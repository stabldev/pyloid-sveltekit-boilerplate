<script lang="ts">
  import { onMount } from 'svelte';
  import { type Snippet } from 'svelte';

  const { children }: { children: Snippet } = $props();
  let base = $state('');

  onMount(async () => {
    base = (await window.pyloid.JSApi.get_production_path()) || '';
  });
</script>

{@render children()}
