<script>
	import { user } from '$lib/stores/userStore.js';
</script>

<section>
	<h1>Какая то инфа</h1>
	<h2>{$user.email}</h2>
	<h2>{$user.token}</h2>
	<h2>{$user.image}</h2>
</section>

<style>
</style>
