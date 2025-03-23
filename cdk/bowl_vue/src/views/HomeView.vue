<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'

defineProps<{
  gameId: string
}>()

</script>

<template>
  <main>
    <TheWelcome />
  </main>
</template>
