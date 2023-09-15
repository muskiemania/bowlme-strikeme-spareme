<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

import DrawCards from './DrawCards.vue'

</script>

<template>
    <div>
        <DrawCards />
    </div>
</template>

<style scoped>


</style>
