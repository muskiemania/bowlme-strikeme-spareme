<script setup lang="ts">

import Seats from './Seats.vue'
import PokerHand from './PokerHand.vue'
import DrawFactory from './DrawFactory.vue'

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

</script>

<template>
    <div>
        <div>
            <span id="game-id">game id</span>
            <Seats />
            <PokerHand />
        </div>
        <DrawFactory />
    </div>
</template>

<style scoped>

#game-id {
    position: absolute;
    top: 0;
    padding-left: 5px;
    color: white;
}

</style>
