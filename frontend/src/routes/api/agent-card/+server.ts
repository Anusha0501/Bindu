import { config } from "$lib/server/config";
import { json, error } from "@sveltejs/kit";

export async function GET() {
	const binduBaseUrl = config.BINDU_BASE_URL;

	if (!binduBaseUrl) {
		return json({
			name: "Bindu Agent",
			description: "No agent configured. Set BINDU_BASE_URL to connect to a Bindu agent.",
			url: null,
			version: null,
			skills: [],
			capabilities: {},
		});
	}

	try {
		// Fetch agent card from Bindu backend (A2A protocol)
		const agentCardUrl = `${binduBaseUrl.replace(/\/$/, "")}/.well-known/agent.json`;
		const response = await fetch(agentCardUrl, {
			headers: {
				Accept: "application/json",
			},
		});

		if (!response.ok) {
			throw new Error(`Failed to fetch agent card: ${response.status}`);
		}

		const agentCard = await response.json();

		return json({
			name: agentCard.name || "Bindu Agent",
			description: agentCard.description || null,
			url: binduBaseUrl,
			version: agentCard.version || null,
			skills: agentCard.skills || [],
			capabilities: agentCard.capabilities || {},
		});
	} catch (e) {
		console.error("Failed to fetch agent card:", e);
		return json({
			name: "Bindu Agent",
			description: "Could not connect to agent",
			url: binduBaseUrl,
			version: null,
			skills: [],
			capabilities: {},
		});
	}
}
