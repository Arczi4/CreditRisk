from app.core.logging_config import get_logger
from app.models.payback_models import PaybackRequest
from app.models.ml_models import ModelSignals
from rag.vector import retriever_service
from rag.prompt_template import template
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from app.models.analysis_models import LlmAnalyseResponse

logger = get_logger(__name__)


class AnalysisService:
    """
    Provides additional insights for future analysis based on credit risk score and porovided data
    """

    def __init__(self):
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = ChatOpenAI(model="gpt-5.4-mini")
        self.chain = self.prompt | self.model | StrOutputParser()
        self.retriever = retriever_service.get_retriever()

    def analyse(
        self, applicant_data: PaybackRequest, model_signals: ModelSignals
    ) -> LlmAnalyseResponse:
        # TODO: Add error handling
        logger.info(f"Analysing application for {applicant_data.request_id}...")

        retrieved_context = self.retriever.invoke(
            self.build_retrieval_query(applicant_data, model_signals)
        )
        analyse_result = self.chain.invoke(
            {
                "applicant_info": applicant_data.model_dump(),
                "model_signals_json": model_signals.model_dump(),
                "retrieved_context": retrieved_context,
            }
        )
        parsed_result = LlmAnalyseResponse.model_validate_json(analyse_result)

        logger.info(f"Analysing application for {applicant_data.request_id} done.")

        return parsed_result

    @staticmethod
    def build_retrieval_query(
        applicant_data: PaybackRequest, model_signals: ModelSignals
    ) -> str:
        return f"""
            Loan application review case.
            Need policy and review guidance for new loan application.
            This is the applicant data:
            {applicant_data.model_dump()}

            These are top factors from the model that predict loan payback probability:
            {model_signals.topPositive.model_dump()}
            
            These are bottom factors from the model that predict loan payback probability:
            {model_signals.topNegative.model_dump()}

            Focus on affordability, credit review, documentation needs, and analyst next steps.
        """


analysis_service = AnalysisService()
