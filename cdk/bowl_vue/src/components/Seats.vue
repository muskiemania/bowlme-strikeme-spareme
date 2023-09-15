<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

import Player from './Player.vue'

const players = ['Paul', 'Sara', 'Sarah']

</script>

<template>
    <div class='poker-table-seats grid-x row align-center'>
        <Player v-for="player in players" :name="player" />
    </div>
</template>

<style scoped>

.poker-table-seats {
    margin-top: 1em;
}

</style>
