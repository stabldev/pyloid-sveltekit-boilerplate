<script lang="ts">
  import { onMount } from 'svelte';
  import { type Snippet } from 'svelte';

  const { children }: { children: Snippet } = $props();
</script>

{@render children()}
