<script setup lang="ts">

import Create from './Create.vue'
import Join from './Join.vue'
import Welcome from './Welcome.vue'

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

console.log(mode);

</script>

<template>
    <div class='join-create'>
        <Create v-show="mode === 'JoinCreate.Create'" />
        <Join v-show="mode === 'JoinCreate.Join'" />
        <Welcome v-show="mode === 'JoinCreate.Welcome'" />
    </div>
</template>

<style scoped>

.join-create {

    font-family: 'carddeck';

    input {
        text-shadow: 2px 2px 3px rgba(0,0,0,0.2),
        -2px 2px 3pc rgba(0,0,0,0.2),
        2px -2px 3px rgba(0,0,0,0.2).
        -2px -2px 3px rgba(0,0,0,0.2);
        background: rgba(0,0,0,0.1);
        border: 4px solid rgba(255,255,255,0.6);
        color: rgba(255,255,255,0.9);
        text-shadow: 2px 2px 3px rgba(0,0,0,0.2),
        -2px 2px 3px rgba(0,0,0,0.2),
        2px -2px 3px rgba(0,0,0,0.2),
        -2px -2px 3px rgba(0,0,0,0.2);

        font-size: 3em;
        padding: 0.5em;
        height: 3em;
    }

    input:focus {
        background: rgba(0,0,0,0.1);
        border: 4px solid rgba(255,255,255,0.9);
    }

    ::-webkit-input-placeholder {
        color: white;
        opacity: 0.8 !important;
    }
    
    :-moz-placeholder {
        color: white;
        opacity: 0.8 !important;
    }

    ::moz-placeholder {
        color: white;
        opacity: 0.8 !important;
    }

    :-ms-input-placeholder {
        color: white;
        opacity: 0.8 !important;
    }
}
        




</style>
