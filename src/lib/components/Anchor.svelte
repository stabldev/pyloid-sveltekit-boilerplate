<script lang="ts">
  import { dev, browser } from '$app/environment';
  import { onMount, type Snippet } from 'svelte';

  let { href, children }: { href: string; children: Snippet } = $props();

  // Add `.html` prefix to href because of `prerender`-ing
  let base = $state('');

  onMount(async () => {
    base = (await window.pyloid.JSApi.get_production_path()) || '';
  });

  if (!dev) href = href + '.html';
  $effect(() => {
    if (!href.startsWith('.')) {
      href = base + href;
    }
  });
</script>

<!-- Hide this link object from prerender -->
{#if browser}
  <a {href}>{@render children?.()}</a>
{/if}
