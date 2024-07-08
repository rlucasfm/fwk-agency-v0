import os
from langchain_openai import ChatOpenAI
from crewai import Agent
from tools import search_tool, search_instagram

max_iters = 10

# ------------------ For using with LLM Studio ------------------
llm = ChatOpenAI()
# ----------------------------------------------------------------

market_analyst_agent = Agent(
    role="Trend Researcher",
    goal="""\
        Make amazing analysis of trends
        and generate valuable in-depth insights to guide
        marketing strategies.""",
    backstory="""\
        As a seasoned trend researcher, you have worked on several
        premier marketing firms. You're specialized on generate insights
        from trends and apply them on marketing.""",
    tools=[
        search_tool,
    ],
    allow_delegation=False,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)

marketing_strategist_agent = Agent(
    role="Chief Marketing Strategist",
    goal="""\
        Understand completely insights about trends to
        formulate amazing marketing strategies.""",
    backstory="""\
        You are the Chief Marketing Strategist at
        a leading digital marketing agency, known for crafting
        bespoke strategies that drive success.""",
    tools=[
        search_tool,
        search_instagram
    ],
    allow_delegation=True,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)

content_creator_agent = Agent(
    role="Creative Content Creator",
    goal="""\
        Develop compelling and innovative content
        for social media campaigns, with a focus on creating
        high-impact Instagram ad copies.""",
    backstory="""\
        As a Creative Content Creator at a top-tier
        digital marketing agency, you excel in crafting narratives
        that resonate with audiences on social media.
        Your expertise lies in turning marketing strategies
        into engaging stories and visual content that capture
        attention and inspire action.""",
    tools=[
        search_tool,
        search_instagram
    ],
    allow_delegation=True,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)

translator = Agent(
    role="Translator",
    goal="""\
        Translate content for social media campaigns.""",
    backstory="""\
        As a Translator at a top-tier
        digital marketing agency, you excel in translating marketing campaigns
        keeping the original intent and tone.
        Your expertise lies in translating marketing campaigns in different languages 
        while keeping the same mood, tone and intent from the original text.""",
    allow_delegation=True,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)

photographer_agent = Agent(
    role="Chief Photographer",
    goal="""\
        Take the most amazing photographs for instagram ads that
        capture emotions and convey a compelling message.""",
    backstory="""\
        As a Chief Photographer at a leading digital marketing
        agency, you are an expert at taking amazing photographs that
        inspire and engage, you're now working on a new campaign for a super
        important customer and you need to take the most amazing photograph.""",
    tools=[
        search_tool,
        search_instagram
    ],
    allow_delegation=False,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)

director_agent = Agent(
    role="Creative Director",
    goal="""\
        Oversee the work done by your team to make sure it's the best
        possible and aligned with the product's goals, review, approve,
        ask clarifying question or delegate follow up work if necessary to make
        decisions""",
    backstory="""\
        You're the Creative Director of leading digital
        marketing specialized in product branding. You're working on a new
        customer, trying to make sure your team is crafting the best possible
        content for the customer.""",
    tools=[
        search_tool,
        search_instagram
    ],
    allow_delegation=True,
    llm=llm,
    verbose=True,
    max_iters=max_iters
)