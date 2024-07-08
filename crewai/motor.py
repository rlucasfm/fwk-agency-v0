
from crewai import Crew
from dotenv import load_dotenv
from agents import market_analyst_agent, marketing_strategist_agent, content_creator_agent, translator, director_agent, photographer_agent
from tasks import MarketingAnalysisTasks

def RunCrew(campaign_task):
    tasks = MarketingAnalysisTasks()
    tasks_analysis = tasks.task_analysis(market_analyst_agent, campaign_task)
    campaign_development = tasks.campaign_development(marketing_strategist_agent, campaign_task)
    write_copy = tasks.instagram_ad_copy(content_creator_agent)

    # --- MONTAR A EQUIPE DE COPY ---
    campaign_crew = Crew(
        agents=[
            market_analyst_agent,
            marketing_strategist_agent,
            content_creator_agent
        ],
        tasks=[
            tasks_analysis,
            campaign_development,
            write_copy
        ],
        verbose=True
    )
    campaign = campaign_crew.kickoff()

    take_photo = tasks.take_photograph_task(photographer_agent, campaign, campaign_task)
    review_photo = tasks.review_photo(director_agent, campaign)

    image_crew = Crew(
        agents=[
            photographer_agent,
            director_agent
        ],
        tasks=[
            take_photo,
            review_photo
        ],
        verbose=True
    )

    images = image_crew.kickoff()

    translate_copy = tasks.translate_copy(translator, campaign_task, campaign)

    translation_crew = Crew(
        agents=[translator],
        tasks=[translate_copy],
        verbose=True
    )

    translated_copy = translation_crew.kickoff()

    # --- APRESENTAR AS CAMPANHAS ---
    return {
        "campaign": translated_copy,
        "images": images
    }