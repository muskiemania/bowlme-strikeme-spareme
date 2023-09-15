<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

import Button from './Button.vue'
import ButtonGroup from './ButtonGroup.vue'

const discard = false;

</script>

<template>
    <div class='draw-cards'>
        <div class='button-overlay'>
            <Button text='Discard' v-show="discard" />
            <Button text='Spare' />
            <Button text='Strike' />
            <ButtonGroup>
                <Button text='+3' />
                <Button text='+4' />
                <Button text='+6' />
                <Button text='Finish' />
            </ButtonGroup>
        </div>
    </div>
</template>

<style scoped>


</style>
