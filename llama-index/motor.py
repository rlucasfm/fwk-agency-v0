from llama_index.llms.openai import OpenAI
from agents import campaign_creator, content_creator, photographer, photography_director, translator
from tasks import execute_task, campaign_creation, content_creation, take_photos, review_photos, translate_copy

llm = OpenAI(model="gpt-3.5-turbo")

agents = {
    "Campaign_Creator": campaign_creator(llm),
    "Content_Creator": content_creator(llm),
    "Translator": translator(llm),
    "Photographer": photographer(llm),
    "Photography_Director": photography_director(llm)
}

def run_agency(campaign_briefing, aditional_info):
    print("------ Executing tasks ------")

    campaign_idea = execute_task(campaign_creation(agents["Campaign_Creator"], campaign_briefing, aditional_info))
    posts_content = execute_task(content_creation(agents["Content_Creator"], campaign_idea, campaign_briefing))
    imagine_photos = execute_task(take_photos(agents['Photographer'], posts_content, campaign_briefing))
    reviewed_photos = execute_task(review_photos(agents['Photography_Director'], posts_content, campaign_briefing, imagine_photos))
    translated_copy = execute_task(translate_copy(agents['Translator'], posts_content, campaign_briefing))

    # print(f"----- First task output -----\n {campaign_idea}")
    # print(f"----- Second task output -----\n {posts_content}")
    # print(f"----- Third task output -----\n {imagine_photos}")
    # print(f"----- Fourth task output -----\n {translated_copy}")

    print("------ Finished ------")
    return({
        "post_content": translated_copy,
        "images": reviewed_photos
    })