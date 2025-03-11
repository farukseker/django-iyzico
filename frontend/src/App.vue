<template>
  <main class="w-full min-h-screen flex flex-col bg-gray-900 text-white">
    <nav class="mx-auto mt-2">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
  <router-view class="mx-auto" />
  </main>
</template>

<style>
</style>
