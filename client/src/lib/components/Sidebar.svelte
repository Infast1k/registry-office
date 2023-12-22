<script>
	import { goto } from '$app/navigation';
	import { get } from 'svelte/store';
	import axios from 'axios';
	import { token, role } from '$lib/stores/userStore.js';

	import '../../app.css';
	import logo from '$lib/images/svelte-logo.svg';
</script>

<nav class="sidebar">
	<header>
		<a href="/">
			<div class="image-text">
				<span class="image">
					<img src={logo} alt="logo" />
				</span>

				<div class="text header-text">
					<span class="name">Registry Office</span>
					<span class="profession">Создай семью с нами</span>
				</div>
			</div>
		</a>
	</header>
	<div class="menu-bar">
		<div class="menu">
			<ul class="menu-links">
				<li class="nav-link active">
					<a href="/">
						<i class="bx bx-home-alt icon" />
						<span class="text nav-text">Главная</span>
					</a>
				</li>
				<li class="nav-link">
					<a
						href="/contracts/"
						on:click={() => {
							goto('/my-contracts/');
						}}
					>
						<i class="bx bx-bar-chart-alt-2 icon" />
						<span class="text nav-text">Все договоры</span>
					</a>
				</li>
				{#if $role === 'user' || $role === 'employee' || $role === 'admin'}
					<li class="nav-link">
						<a href="/my-contracts/">
							<i class="bx bx-bell icon" />
							<span class="text nav-text">Мои договоры</span>
						</a>
					</li>
					<li class="nav-link">
						<a href="/relatives/">
							<i class="bx bx-pie-chart-alt icon" />
							<span class="text nav-text">Родственники</span>
						</a>
					</li>
				{/if}
				{#if $role === 'employee' || $role === 'admin'}
					<li class="nav-link">
						<a href="/employee/contracts/">
							<i class="bx bx-heart icon" />
							<span class="text nav-text">Упр. договорами</span>
						</a>
					</li>
				{/if}
				{#if $role === 'admin'}
					<li class="nav-link">
						<a href="/admin/">
							<i class="bx bx-wallet icon" />
							<span class="text nav-text">Пользователи</span>
						</a>
					</li>
				{/if}
				{#if $token}
					<li class="nav-link">
						<a href="/profile/">
							<i class="bx bx-wallet icon" />
							<span class="text nav-text">Личный кабинет</span>
						</a>
					</li>
				{/if}
			</ul>
		</div>
		{#if $token}
			<div class="bottom-content">
				<li class="">
					<a
						href="#!"
						on:click={() => {
							const empty = ' ';
							axios
								.post('http://localhost:8000/api/v1/auth/token/logout/', empty, {
									headers: {
										Authorization: `Token ${get(token)}`
									}
								})
								.then((response) => {
									// Удаление токена
									token.set('');
									role.set('');
									goto('/');
								})
								.catch((errors) => {
									console.log(errors);
								});
						}}
					>
						<i class="bx bx-log-out icon" />
						<span class="text nav-text">Выйти</span>
					</a>
				</li>
			</div>
		{:else}
			<div class="bottom-content">
				<li class="">
					<a href="/login">
						<i class="bx bx-log-out icon" />
						<span class="text nav-text">Войти</span>
					</a>
				</li>
			</div>
		{/if}
	</div>
</nav>

<style>
	a {
		text-decoration: none;
	}
	.sidebar {
		top: 0;
		left: 0;
		height: 100%;
		width: 250px;
		padding: 10px 14px;
		background: var(--sidebar-color);
	}

	.sidebar .text {
		font-size: 16px;
		font-weight: 500;
		color: var(--text-color);
	}

	.sidebar .image {
		min-width: 60px;
		display: flex;
		align-items: center;
	}

	.sidebar li {
		height: 50px;
		margin-top: 10px;
		list-style: none;
		display: flex;
		align-items: center;
	}

	.sidebar li .icon {
		display: flex;
		align-items: center;
		justify-content: center;
		min-width: 60px;
		font-size: 20px;
	}

	.sidebar li .icon,
	.sidebar li .text {
		color: var(--text-color);
		transition: var(--tran-02);
	}

	.sidebar header {
		position: relative;
	}

	.sidebar .image-text img {
		width: 40px;
		border-radius: 6px;
	}

	.sidebar header .image-text {
		display: flex;
		align-items: center;
	}

	header .image-text .header-text {
		display: flex;
		flex-direction: column;
	}

	.header-text .name {
		font-weight: 600;
	}

	.header-text .profession {
		margin-top: -2px;
	}

	.sidebar li a {
		height: 100%;
		width: 100%;
		display: flex;
		align-items: center;
		text-decoration: none;
		border-radius: 6px;
		transition: var(--tran-04);
	}

	.sidebar li a:hover {
		background: var(--primary-color);
	}

	.sidebar li a:hover .icon,
	.sidebar li a:hover .text {
		color: var(--sidebar-color);
	}

	.sidebar .menu-bar {
		height: calc(100% - 50px);
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
</style>
