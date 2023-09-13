<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { store } from './store.ts'

import JoinCreate from './components/JoinCreate.vue'
//import DisplayQrCode from './components/DisplayQrCode.vue'
//import Waiting from './components/Waiting vue'
//import PokerTable from './components/PokerTable.vue'
//import Results from './components/Results.vue'

</script>

<template>
    <div class="poker-table">
      <JoinCreate />
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
