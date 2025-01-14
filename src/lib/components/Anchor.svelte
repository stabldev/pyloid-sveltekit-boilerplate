<script lang="ts">
  import { dev, browser } from '$app/environment';
  import { type Snippet } from 'svelte';

  let { href, children }: { href: string; children: Snippet } = $props();
  // Add `.html` prefix to href because of `prerender`-ing

  if (!dev) href = href + '.html';
</script>

<!-- Hide this link object from prerender -->
{#if browser}
  <a {href}>{@render children()}</a>
{/if}
