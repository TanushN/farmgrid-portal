<script>
    import { Route } from 'svelte-navigator';
    import { user } from '../stores';
    import Login from './login.svelte';

    export let path;
    export let component;

    $: isLoggedIn = $user;
</script>

{#if isLoggedIn || path === "/signup"}
    <Route path={path} component={component} />
{:else}
    <Route path={path} component={Login} />
{/if}
