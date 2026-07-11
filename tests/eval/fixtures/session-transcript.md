Working-session log (condensed):

User: Let's build a tool that catches failing webhooks before customers notice.
Assistant: Created the delivery inspector first: it records every attempt with the full payload and response code.
User: Good. Add retry visibility.
Assistant: Then we added retry timelines, so each delivery shows its attempts in order with timing.
User: We also need alerts.
Assistant: Finally wired up Slack alerts: a channel ping fires when an endpoint's failure rate crosses a threshold. We named the tool Relay. Pricing is not decided yet.
