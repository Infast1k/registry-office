<script>
	import '../../app.css';
	import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<main>
	<div class="sidebar">
		<Sidebar />
	</div>
	<div class="container">
		<slot />
	</div>
</main>

<style>
	main {
		height: 100vh;
		background: var(--body-color);
		display: flex;
	}
	.sidebar {
		flex: 1;
	}
	.container {
		flex: 10;
	}
</style>
