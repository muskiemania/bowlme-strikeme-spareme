<script setup lang="ts">

import { useState, useActions, useGetters } from 'vuex-composition-helpers/dist'
const { changeView } = useActions(['changeView'])
const { mode } = useState(['mode']);

import Cards from './Cards.vue'

</script>

<template>
    <div class='grid-x row'>
        <div class='small-12 columns'>
            <div class='grid-x row align-center'>
                <Cards />
            </div>
        </div>
    </div>
</template>

<style scoped>


</style>
