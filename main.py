import argparse

from rg import AutoApplyModel


def create_resume_cv(url, master_data, api_key, provider, model, downloads_dir):
    """
    Creates a resume or CV using the Job-LLM model.

    Args:
        url (str): The URL of the job posting or description.
        master_data (dict): The master data containing information about the candidate.
        api_key (str): The API key for OpenAI.
        provider (str): The LLM provider to use. Currently, only "OpenAI, Gemini" is supported.
        model (str): The LLM model to use.
        downloads_dir (str): The directory where the generated resume or CV will be saved.

    Returns:
        None
    """
    job_llm = AutoApplyModel(api_key, provider, model, downloads_dir)
    job_llm.resume_cv_pipeline(url, master_data)


if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add the required arguments

    parser.add_argument("-u", "--url", help="URL of the job posting")
    parser.add_argument("-m", "--master_data", help="Path of user's master data file.")
    parser.add_argument("-k", "--api_key", default="os", help="LLM Provider API Keys")
    parser.add_argument("-d", "--downloads_dir", help="Give detailed path of folder")
    parser.add_argument("-p", "--provider", help="LLM provider name. support for openai, gemini")
    parser.add_argument("-l", "--model", help="LLM model name")

    # Parse the arguments
    args = parser.parse_args()

    create_resume_cv(
        args.url, args.master_data, args.api_key, args.provider, args.model, args.downloads_dir
    )