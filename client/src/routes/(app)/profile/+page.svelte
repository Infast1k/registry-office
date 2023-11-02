<script>
	export let data;
</script>

<main class="container">
	<h1>asdfdsf</h1>
	<h1>{data.post.title}</h1>
	<div class="contact_info">
		<div class="bio">ФИО и тд</div>
		<div class="passport">паспорт</div>
	</div>
	<div class="family">Тут инфа о родственниках</div>
</main>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		background: red;
	}

	.contact_info {
		display: flex;
		justify-content: space-between;
		background: green;
	}
</style>
