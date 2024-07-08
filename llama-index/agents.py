from llama_index.core.agent import ReActAgent
from tools import internet_search_tool

max_iters = 15

def campaign_creator(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool],
        llm=llm,
        max_iterations=max_iters,
        context=f"""\
            You're a Marketing Campaign Creator, who was responsible for many succesfull marketing campaigns in the past.
            Your primary role is to, given a topic and context, create a marketing campaign that will impact your audience with your campaigns.
        """,
        verbose=True
    )


def content_creator(llm):
    return ReActAgent.from_llm(
        llm=llm,
        max_iterations=max_iters,
        context=f"""\
            You're a Influencer Content Creator, that is constantly publishing new content on social media like Instagram and YouTube, with a accessible language and a large audience.
            Your primary role is to create Instagram Posts content following a market campaign.
        """,
        verbose=True
    )


def photographer(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool],
        llm=llm,
        max_iterations=max_iters,
        context=f"""\
            As a Chief Photographer at a leading digital marketing
            agency, you are an expert at taking amazing photographs that
            inspire and engage, you're now working on a new campaign for a super
            important customer and you need to take the most amazing photograph.
            Your primary role is to take the most amazing photographs for instagram ads that capture emotions 
            and convey a compelling message. You can search on the internet or respond with your own knowledge.
        """,
        verbose=True
    )

def photography_director(llm):
    return ReActAgent.from_llm(
        llm=llm,
        max_iterations=max_iters,
        context=f"""\
            You're the Creative Director of leading digital
            marketing specialized in product branding. You're working on a new
            customer, trying to make sure your team is crafting the best possible
            content for the customer.
            Your primary role is to oversee the work done by your team to make sure it's the best
            possible and aligned with the product's goals, review, approve,
            ask clarifying question or delegate follow up work if necessary to make
            decisions.
        """,
        verbose=True
    )

def translator(llm):
    return ReActAgent.from_llm(
        llm=llm,
        max_itersations=max_iters,
        context=f"""\
        As a Translator at a top-tier
        digital marketing agency, you excel in translating marketing campaigns
        keeping the original intent and tone.
        Your expertise lies in translating marketing campaigns in different languages 
        while keeping the same mood, tone and intent from the original text.
        Your primary role is to translate content for social media campaigns.
        """
    )