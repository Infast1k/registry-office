<script>
	import Image from '$lib/images/пугна.jpg';
</script>

<main>
	<div class="container">
		<h1>Личный кабинет</h1>
		<img src="$lib/images/пугна.jpg" alt="" />
		<div class="contact_info">
			<div class="bio">
				<table>
					<thead>
						<tr>
							<th colspan="2">Персональные данные</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>Фамилия</td>
							<td>Насонов</td>
						</tr>
						<tr>
							<td>Имя</td>
							<td>Михаил</td>
						</tr>
						<tr>
							<td>Отчество</td>
							<td>Игоревич</td>
						</tr>
						<tr>
							<td>Телефон</td>
							<td>89010557301</td>
						</tr>
						<tr>
							<td>Дата рождения</td>
							<td>10-12-2003</td>
						</tr>
						<tr>
							<td>Город</td>
							<td>Ярославль</td>
						</tr>
						<tr>
							<td>Улица</td>
							<td>Чайковского</td>
						</tr>
						<tr>
							<td>Дом</td>
							<td>78/19</td>
						</tr>
						<tr>
							<td>Квартира</td>
							<td>121</td>
						</tr>
					</tbody>
				</table>
			</div>

			<div class="passport">паспорт</div>
		</div>
		<div class="family">Тут инфа о родственниках</div>
	</div>
</main>

<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.container {
		margin-top: 20px;
		border-radius: 10px;
		background: var(--sidebar-color);
		border: var(--primary-color) dashed 1px;
		width: 65%;
		text-align: center;
	}

	.contact_info {
		display: flex;
		justify-content: space-between;
	}

	.bio {
		display: block;
		align-items: center;
	}
</style>
