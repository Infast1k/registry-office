<script>
	import '../../app.css';
	import Header from '../../lib/components/Header.svelte';
</script>

<div class="flex justify-start bg-main">
	<Header />
	<div class="main">
		<slot />
	</div>
</div>
