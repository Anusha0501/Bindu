<script lang="ts">
	import { onMount } from "svelte";

	let rawAgentJson = $state<string>("");
	let agentLoading = $state(true);
	let agentError = $state<string | null>(null);

	onMount(async () => {
		try {
			const res = await fetch("/api/agent-card");
			if (res.ok) {
				const data = await res.json();
				rawAgentJson = JSON.stringify(data, null, 2);
			} else {
				agentError = "Could not load agent info";
			}
		} catch (e) {
			agentError = "Agent not connected";
		} finally {
			agentLoading = false;
		}
	});
</script>

<div class="flex flex-col gap-4">
	<div class="flex items-center justify-between">
		<h1 class="text-xl font-bold text-gray-900 dark:text-white">Agent Info</h1>
		{#if !agentLoading && !agentError}
			<button
				class="rounded-lg bg-gray-100 px-3 py-1.5 text-xs font-medium text-gray-700 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600"
				onclick={() => navigator.clipboard.writeText(rawAgentJson)}
			>
				📋 Copy JSON
			</button>
		{/if}
	</div>

	{#if agentLoading}
		<div class="flex items-center gap-2 text-gray-500">
			<span class="size-2 animate-pulse rounded-full bg-gray-400"></span>
			Loading agent info...
		</div>
	{:else if agentError}
		<div class="rounded-lg border border-red-200 bg-red-50 p-4 dark:border-red-800 dark:bg-red-900/20">
			<p class="text-sm text-red-600 dark:text-red-400">{agentError}</p>
		</div>
	{:else}
		<pre
			class="overflow-x-auto rounded-lg bg-gray-100 p-4 font-mono text-xs text-gray-800 dark:bg-gray-800 dark:text-gray-300">{rawAgentJson}</pre>
	{/if}
</div>
