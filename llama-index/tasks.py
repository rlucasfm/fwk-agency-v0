def Task(description, agent, expected_output):
    return {
        "agent": agent,
        "query": f"""\
            {description}

            Your final answear must be {expected_output}
        """
    }

def execute_task(task):
    curr_agent = task["agent"]
    return curr_agent.query(task["query"])


def campaign_creation(agent, briefing, aditional_info):
     return Task(
        agent=agent, 
        description=f"""\
            Analyze the briefing in the <brief> tag: <brief>{briefing}</brief>
            Extra info provided about it are provided inside the <add> tag: <add>{aditional_info}</add>

            Search the internet to try to understand deply the topic from the briefing and what trends relate to it.
            Using what you found about the briefing and trends, define target audience, marketing objectives, and the main messages of the campaign.

            If you can't find any useful info in the internet, answear with your own knowledge.

            Your final report should be a description of the campaign.

            Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
        """,
        expected_output="""\
            A description of the campaign as the example, substituting between the asterisks:
            *Campaign Name*
            - Target Audience: ...
            - Objectives: ...
            - Messages: ...
        """
    )


def content_creation(agent, campaign_info, briefing):
    return Task(
        agent=agent, 
        description=f"""\
            Given the campaign information inside the <camp> tags: <camp>{campaign_info}</camp>\n
            Created for the briefing inside the <brief> tags: <brief>{briefing}</brief>

            Create 5 posts for the campaign, considering the target audience, objectives and message described.
            The copy should have at least 2 paragraphs of content, and a minimal of 40 words. Use at least 3 hashtags related to the topic.
        """,
        expected_output="""Each posts content in the format:
            Post Title: ...
            Copy: ...
            ------------------
        """
    )

def take_photos(agent, copy, briefing):
    return Task(
        agent=agent,
        description=f"""\
            You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an instagram post
			regarding the product, you have the following copy:
			{copy}

			This are the briefing of the campaign you are working with: {briefing}.
			Imagine what the photo you wanna take describe it in a paragraph.
			Here are some examples for you follow:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product on the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
        """,
        expected_output="3 options of photographs, each with 1 paragraph describing the photograph exactly, in english."
    )

def review_photos(agent, copy, briefing, photos):
    return Task(
        agent=agent,
        description=f"""\
            Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			This is the campaign posts and copies: {copy}.
			That posts were created for this briefing: {briefing}.
            These are the description of the photos: {photos}

			Here are some examples on how the final photographs should look like:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
        """,
        expected_output="""
        3 reviewd options of photographs, describing exaclty how the photograph is in a very detailed way.
        Each description should start with "Imagine ".
        Format your response as a list of the descriptions, separated by new lines, as the following example:
        1. ...
        2. ...
        3. ...
        """
    )

def translate_copy(agent, copy, briefing):
    return Task(
        agent=agent,
        description=f"""\
        You are translating instagram ad copies for the briefing inside the <brief> tags: <brief>{briefing}</brief>.
        The marketing copy is inside the <copy> tags: <copy>{copy}</copy>
                    
        Translate the copy to the same language as the briefing. Keeping the same tone, intent and mood.
        """,
        expected_output="""
        The translated ad copies ONLY. 
        Format your response as a list of posts separed by new lines, like the following example, 
        replacing the <title> with the actual title, and the <copy> with the actual copy:
        1. <title>: <copy>
        """
    )