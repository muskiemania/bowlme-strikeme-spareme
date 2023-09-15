<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { toggleCard } = useActions(['toggleCard'])
const { mode } = useState(['mode']);

import Card from './Card.vue'

const { hand } = useState(['hand']);

</script>

<template>
    <div class='cards-collection grid-x row'>
        <Card v-for="(card, i) in hand" :card='card.card' :index='i' :selected="card.selected" @toggle="toggleCard" />
    </div>
</template>

<style scoped>

.cards-collection {

    margin-top: 40px;
    .a-card.card-1 {
        margin-left: auto;
    }
}

</style>
