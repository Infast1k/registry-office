<script>
	import '../../app.css';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<main>
	<Sidebar />
	<slot />
</main>

<style>
	main {
		height: 100vh;
		background: var(--body-color);
	}
</style>
