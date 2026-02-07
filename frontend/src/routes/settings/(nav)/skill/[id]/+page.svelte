<script lang="ts">
	import { onMount } from "svelte";
	import { page } from "$app/state";

	type AgentSkill = {
		id: string;
		name: string;
		description?: string;
		inputSchema?: Record<string, unknown>;
		outputSchema?: Record<string, unknown>;
	};

	let skill = $state<AgentSkill | null>(null);
	let loading = $state(true);
	let error = $state<string | null>(null);

	onMount(async () => {
		const skillId = page.params.id;
		try {
			const res = await fetch("/api/agent-card");
			if (res.ok) {
				const data = await res.json();
				skill = data.skills?.find((s: AgentSkill) => s.id === skillId) || null;
				if (!skill) {
					error = "Skill not found";
				}
			} else {
				error = "Could not load skill";
			}
		} catch (e) {
			error = "Agent not connected";
		} finally {
			loading = false;
		}
	});
</script>

<div class="flex flex-col gap-6">
	{#if loading}
		<div class="flex items-center gap-2 text-gray-500">
			<span class="size-2 animate-pulse rounded-full bg-gray-400"></span>
			Loading skill...
		</div>
	{:else if error}
		<div class="rounded-lg border border-red-200 bg-red-50 p-4 dark:border-red-800 dark:bg-red-900/20">
			<p class="text-sm text-red-600 dark:text-red-400">{error}</p>
		</div>
	{:else if skill}
		<div>
			<div class="flex items-center gap-2">
				<span
					class="rounded bg-green-100 px-2 py-1 text-xs font-medium text-green-700 dark:bg-green-900/30 dark:text-green-400"
					>skill</span
				>
				<h1 class="text-xl font-bold text-gray-900 dark:text-white">
					{skill.name}
				</h1>
			</div>
			{#if skill.id}
				<p class="mt-1 font-mono text-xs text-gray-500">{skill.id}</p>
			{/if}
		</div>

		{#if skill.description}
			<div>
				<h3 class="mb-2 text-sm font-semibold text-gray-700 dark:text-gray-300">Description</h3>
				<p class="text-sm leading-relaxed text-gray-600 dark:text-gray-400">
					{skill.description}
				</p>
			</div>
		{/if}

		{#if skill.inputSchema}
			<div>
				<h3 class="mb-2 text-sm font-semibold text-gray-700 dark:text-gray-300">Input Schema</h3>
				<pre
					class="overflow-x-auto rounded-lg bg-gray-100 p-4 font-mono text-xs text-gray-800 dark:bg-gray-800 dark:text-gray-300">{JSON.stringify(skill.inputSchema, null, 2)}</pre>
			</div>
		{/if}

		{#if skill.outputSchema}
			<div>
				<h3 class="mb-2 text-sm font-semibold text-gray-700 dark:text-gray-300">Output Schema</h3>
				<pre
					class="overflow-x-auto rounded-lg bg-gray-100 p-4 font-mono text-xs text-gray-800 dark:bg-gray-800 dark:text-gray-300">{JSON.stringify(skill.outputSchema, null, 2)}</pre>
			</div>
		{/if}
	{/if}
</div>
