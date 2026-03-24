from app.core.logging_config import get_logger
from app.models.payback_models import PaybackRequest
from rag.vector import retriever
from rag.prompt_template import template
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI
from app.models.analysis_models import LlmAnalyseResponse

logger = get_logger(__name__)


class AnalysisService:
    """
    Provides additional insights for future analysis based on credit risk score and porovided data
    """

    def __init__(self):
        self.prompt = ChatPromptTemplate(template)
        self.model = OpenAI(model="gpt-5.4-mini")
        self.chain = self.prompt | self.model

    def analyse(
        self, applicant_data: PaybackRequest, model_signals: dict
    ) -> LlmAnalyseResponse:
        # TODO: Add error handling
        logger.info(f"Analysing application for {applicant_data.request_id}...")

        retrieved_context = retriever.invoke(
            self.build_retrieval_query(applicant_data, model_signals)
        )
        analyse_result = self.chain.invoke(
            {
                "applicant_info": applicant_data.model_dump(),
                "model_signals_json": model_signals,
                "retrieved_context": retrieved_context,
            }
        )
        parsed_result = LlmAnalyseResponse.model_validate_json(analyse_result)

        logger.info(f"Analysing application for {applicant_data.request_id} done.")

        return parsed_result

    @staticmethod
    def build_retrieval_query(
        applicant_data: PaybackRequest, model_signals: dict
    ) -> str:
        return f"""
            Loan application review case.
            Need policy and review guidance for new loan application.
            This is the applicant data:
            {applicant_data.model_dump()}

            These are top factors from the model that predict loan payback probability:
            {model_signals.get("top_factors", [])}
            
            Focus on affordability, credit review, documentation needs, and analyst next steps.
        """


analysis_service = AnalysisService()
