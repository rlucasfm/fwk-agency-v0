from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def task_analysis(self, agent, marketing_topics):
		return Task(
			description=dedent(f"""\
			Analyze the given marketing topics: {marketing_topics}.

			Focus on identifying trends, popular topics,
			and what people are talking related to the marketing topics.

			Your final report should clearly articulate the
			latest trends, its market appeal,
			and ideas explaining how to tackle these trends.

			Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
			"""),
			agent=agent,
			expected_output="A detailed report about the given topics."
		)

	def campaign_development(self, agent, marketing_topics):
		return Task(
			description=dedent(f"""\
			You're creating a targeted marketing campaign for the topics: {marketing_topics}.

			To start this campaing we will need a strategy and creative content ideas.
			It should be meticulously designed to captivate and engage
			the product's target audience.

			Based on your ideas your co-workers will create the content for the campaign.

			Your final answer MUST be ideas that will resonate with the audience and
			also include ALL context you have about the product and the customer.
			
			Your final answear MUST be in the same language of campaign topics.
			"""),
			agent=agent,
			expected_output="A list of ideas that includes context and is awesome for the audience."
		)

	def instagram_ad_copy(self, agent):
		return Task(
			description=dedent("""\
			Craft an engaging Instagram post copy.
			The copy should be punchy, captivating, concise,
			and aligned with the product marketing strategy.

			Focus on creating a message that resonates with
			the target audience and highlights the product's
			unique selling points.

			Your ad copy must be attention-grabbing and should
			encourage viewers to take action, whether it's
			visiting the website, making a purchase, or learning
			more about the product.

			Your final answer MUST be 3 options for an ad copy for instagram that
			not only informs but also excites and persuades the audience.
			"""),
			agent=agent,
			expected_output="3 options for an ad copy for instagram."
		)
	
	def translate_copy(self, agent, marketing_topics, campaign_copy):
		return Task(
			description=dedent("""\
			You are translating instagram ad copies for the topics: {marketing_topics}.
			The marketing copy is: {campaign_copy}
					  
			Translate the copy to the same language as the campaign topics. Keeping the same tone, intent and mood.
			"""),
			agent=agent,
			expected_output="The translated ad copies ONLY."
		)


	def take_photograph_task(self, agent, copy, campaign):
		return Task(
			description=dedent(f"""\
			You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an instagram post
			regarding the product, you have the following copy:
			{copy}

			This are the topics you are working with: {campaign}.
			Imagine what the photo you wanna take describe it in a paragraph.
			Here are some examples for you follow:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product on the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
			"""),
			agent=agent,
			expected_output="3 options of photographs, each with 1 paragraph describing the photograph exactly"
		)

	def review_photo(self, agent, campaign):
		return Task(
			description=dedent(f"""\
			Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			This are the topics you are working with: {campaign}.

			Here are some examples on how the final photographs should look like:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
			"""),
			agent=agent,
			expected_output="3 reviewd options of photographs, describing exaclty how the photograph is in a very detailed way."
		)