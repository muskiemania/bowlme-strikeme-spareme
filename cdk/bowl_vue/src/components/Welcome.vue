<script setup lang="ts">

import { useActions } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])

import Button from './Button.vue'

</script>

<template>
    <div class='welcome'>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Create Game' @click="changeView('JoinCreate.Create')" />
            </div>
        </div>
        <div class='grid-x row align-center'>
            <div class='column'>
                <Button text='Join Game' @click="changeView('JoinCreate.Join')" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.welcome {
    
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translateX(-50%) translateY(-50%);
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}

.welcome .draw-button {
    float: none;
    margin-right: 0;
    font-size: 3em;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
}

</style>
