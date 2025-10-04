import openai

class StatusSummarizer:
    def __init__(self, openai_api_key, model="gpt-4", temperature=0.7):
        self.api_key = openai_api_key
        self.model = model
        self.temperature = temperature

    def __call__(self, state):
        trello_cards = state.get("trello_cards", [])
        if not trello_cards:
            raise ValueError("No Trello cards found in state")

        prompt = (
            "Summarize the following Trello tasks into a weekly status report:\n\n"
            + str(trello_cards)
        )

        response = openai.ChatCompletion.create(
            api_key=self.api_key,
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a project manager assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature
        )

        summary = response["choices"][0]["message"]["content"]
        return {**state, "status_summary": summary}
