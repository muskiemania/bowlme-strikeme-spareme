<script setup lang="ts">
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { mode } = useState(['mode']);

import JoinCreate from './components/JoinCreate.vue'
import Pregame from './components/Pregame.vue'
import PokerGame from './components/PokerGame.vue'

const route = useRoute();
console.log(route.query.gameId);


</script>

<template>
    <div class="poker-table">
      <JoinCreate v-show="mode.startsWith('JoinCreate')" />
      <Pregame v-show="mode.startsWith('Pregame')" /> 
      <PokerGame v-show="mode.startsWith('PokerGame')" />


    </div>
</template>

<style scoped>
.poker-table {
    width: 100%;
    height: 100vh;
    overflow: hidden;

    background: -webkit-radial-gradient(#00ff00, green);
    background: -o-radial-gradient(#00ff00, green);
    background: -moz-radial-gradient(#00ff00, green);
    background: radial-gradient(#00ff00, green);
}

</style>
