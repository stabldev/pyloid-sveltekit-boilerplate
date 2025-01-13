<script lang="ts">
    import { onMount } from 'svelte';
    import { type Snippet } from 'svelte';

    let base = $state('');
    onMount(async () => {
        base = (await window.pyloid.JSApi.get_production_path()) || '';
    });

    const { children }: { children: Snippet } = $props();
</script>

<svelte:head>
    <base href={base} />
</svelte:head>

{@render children?.()}
