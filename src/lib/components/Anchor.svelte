<script lang="ts">
  import { dev } from '$app/environment';
  import type { Snippet } from 'svelte';

  let { href, children }: { href: string; children: Snippet } = $props();

  if (!dev) href = href + '.html';
</script>

<a {href}>{@render children?.()}</a>
