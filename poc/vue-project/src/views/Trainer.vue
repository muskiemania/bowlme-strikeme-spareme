<template>

    <div id="app">
        <!-- 
            TOUCH CONTAINER
            Parent container for area that's responsive to taps and swipes
        -->
        <div id="touch-container">
            <!--
                RENDERED ITEMS FLEXBOX
                A flexbox container that displays items horizontally & centered
            -->
            <div
                id="rendered-items-flexbox"
                :class="displayStore.transitionClass"
                :style="{transform: displayStore.transformStyle}"
            >
                <!-- 
                    RENDERED ITEM
                    Only 3 items will be rendered at a time (or 1 item if only 1 in array)
                    renderedItems includes the previous, current, & next items
                    It's important that each item has a stable key so Vue can track it
                -->
                <div
                    v-for="item in displayStore.renderedItems"
                    :id="item.key"
                    :key="item.key"
                    class="rendered-item"
                >
                    <!-- 
                        ITEM CONTENT
                        Whatever content or component you're displaying
                    -->
                    <div class="item-content" :class="item.id"></div>
                </div>
            </div>

            <!--
                LEFT & RIGHT TOUCH AREAS
                Non-visible divs over left & right sides of screen that can be tapped to change slide
            -->
            <div
                class="touch-tap-left"
                role="button"
                aria-label="Previous"
                tabindex="0"
                @click="displayStore.previous"
                @keyup.enter="displayStore.previous"
                @keyup.space="displayStore.previous"
            >
            <!--   
                LEFT EDGE SHAPE
                Edge animation when reaching end of array, otherwise loops infinitely (optional)
            -->
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                viewBox="0 0 10 100"
                height="100%"
                width="40px"
                preserveAspectRatio="none"
                class="left-edge-shape"
                :class="displayStore.transitionClass"
                :style="{transform: 'scaleX(' + displayStore.leftEdgeScale + ')'}"
            >
                <path d="M0,0v100h5.2c3-14.1,4.8-31.4,4.8-50S8.2,14.1,5.2,0H0z" />
            </svg>
        </div>

        <div
            class="touch-tap-right"
            role="button"
            aria-label="Next"
            tabindex="0"
            @click="displayStore.next"
            @keyup.enter="displayStore.next"
            @keyup.space="displayStore.next"
        >
            <!-- RIGHT EDGE SHAPE-->
            <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                viewBox="0 0 10 100"
                height="100%"
                width="40px"
                preserveAspectRatio="none"
                class="right-edge-shape"
                :class="displayStore.transitionClass"
                :style="{transform: 'scaleX(' + displayStore.rightEdgeScale + ')'}"
            >
                <path
                    d="M10,100V0L4.8,0C1.8,14.1,0,31.4,0,50c0,18.6,1.8,35.9,4.8,50H10z"
                />
            </svg>
        </div>
    </div>
</div>
    
<!-- OLD CODE 


    <div class='loading' v-if='display.isLoading.value'>
        <span>Loading...</span>
    </div>

    <div class="header">
        <span>
            <button :disabled='!display.getGameLeft'>&lt;&lt;</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='leftFrameDisabled' @click='prevFrame'>Previous Frame</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='rightFrameDisabled' @click='nextFrame'>Next Frame</button>
        </span>&nbsp;|&nbsp; 
        <span>
            <button :disabled='!display.getGameRight'>&gt;&gt;</button>
        </span>
    </div>
    <div class='scoreboard'>
        <span class='frame'>Frame {{ display.getFrameNumber }}</span>
        <div class='score'>

            <table class='box'>
                <tbody>
                    <tr>
                        <td v-for="t, i in display.getFrameThrows.value" :class="i > 0 ? 'box' : 'none'">
                            {{ t }}
                        </td>
                    </tr>
                    <tr>
                        <td colspan='display.getFrameNumber.value === 10 ? 3 : 2'>
                            {{ display.getFrameScore }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div>
        <div class='flippable'i @click='checkMe'>
            <template v-for='url in display.getAnalysis.value'>
                <img :src="url" height="600" width="140" />
            </template>
        </div>
    </div>


    <div class='collapsed-panel' @click='togglePanel'>
        Open Me
    </div>
    <div class='slide-up-panel'>
        <transition name='slide-up'>
            <div v-if='display.getSliderIsOpen.value' class='slide-up-panel'>
                <div class='panel-content'>
                    <h1>Enter data</h1>
                    <div class='pins'>
                        <template v-for='(p, i) in [7,8,9,10]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [4, 5, 6]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [2, 3]'>
                            <template v-if='i > 0'>&nbsp;&nbsp;&nbsp;</template>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>
                        <br />

                        <template v-for='(p, i) in [1]'>
                            <span @click='clickPins(p)' :class='pinsClassname(p)'>{{p}}</span>
                        </template>

                    </div>
                    <div class='pinsInput'>
                        <label for="pins">Pins</label><input v-model='pinsBinding' /><br /><button @click='usePins'>Use Pins</button> <button @click='spare'>Spare</button> <button @click='strike'>Strike</button>
                    </div>
                    <div class="analysisInput">
                        <label class="left" @click='toggleAnalysis(1)'>Pin Exit</label>
                        <input name="pinExit" v-model='pinExitBinding' :disabled='!analysis.pexOn.value' />
                        <input name="arrows" v-model='arrowsBinding' :disabled='!analysis.arrowsOn.value' />
                        <label @click='toggleAnalysis(5)'>Arrows</label>
                        <br style="clear: both" />
                        <label class="left" @click='toggleAnalysis(2)'>Pin Enter</label>
                        <input name="pinEnter" v-model='pinEnterBinding' :disabled='!analysis.penOn.value' />
                        <input name="slide" v-model='slideBinding' :disabled='!analysis.slideOn.value' />
                        <label @click='toggleAnalysis(6)'>Slide</label>
                        <br style="clear: both" />
                        <label class="left" @click='toggleAnalysis(3)'>Break Pt.</label>
                        <input name="breakPoint" v-model='breakPointBinding' :disabled='!analysis.breakPtOn.value'/>
                        <input name="startDots" v-model='startDotsBinding' :disabled='!analysis.startDotsOn.value' />
                        <label @click='toggleAnalysis(7)'>Start Dots</label>
                        <br style="clear: both" />
                        <label class="left" @click='toggleAnalysis(4)'>Break Dist.</label>
                        <input name="breakPoint" v-model='breakDistanceBinding' :disabled='!analysis.breakDistOn.value' />
                        <input name="startDist" v-model='startDistanceBinding' :disabled='!analysis.startDistOn.value' />
                        <label @click='toggleAnalysis(8)'>Start Dist.</label>
 
                        <br style="clear: both" />
                    </div>
            
                    <div class='submit'>
                        <button @click='submitThrow'>Submit</button>&nbsp;&nbsp;&nbsp;<button @click='togglePanel'>Close Me</button>
                    </div>
                </div>
            </div>
        </transition>
    </div>

-->

</template>

<style>
    
    /* Note: This example shows the content as fullscreen with only one item displayed at once
    Adjust sizing to fit your content/use case */
    body {
        min-height: 100vh;
        width: 100vw;
        background-color: white;
    }

    #touch-container {
        position: relative;
        min-width: 100%;
        height: 100%;
        overflow-x: hidden;
    }

    #rendered-items-flexbox {
        display: flex;
        justify-content: center;
        height: 100vh;
        min-height: fit-content;
        width: 100vw;
        box-sizing: border-box;
        touch-action: pan-y; 
        
        /* Disables automatic browser control of touches, except vertical scrolling */
    }

    /* Removes all translation effects for those who prefer less animation */
    @media (prefers-reduced-motion: reduce) {
        #rendered-items-flexbox {
            transform: none !important;
        }
    }

    /* Transition classes */
    .transition-initial {
        transition: transform 0s ease;
    }

    .transition-item {
        transition: transform 250ms cubic-bezier(0.0, 0.0, 0.2, 1); 
        /* ease-out timing function */
    }

    .transition-edge {
        transition: transform 500ms ease-out;
    }
 
    .rendered-item {
        height: 100%;
        min-height: 500px;
        min-width: 100%;
        width: 100%;
        box-sizing: border-box;
    }

    .item-content {
        min-height: 500px;
        height: 100%;
        width: 100vw;
        margin: 0 auto;
        box-sizing: border-box;
    }


    /* Left and right tap targets */
    .touch-tap-left,
    .touch-tap-right {
        position: absolute;
        top: 0;
        width: 20%;
        height: 100%;
    }

    .touch-tap-left {
        left: 0;
    }

    .touch-tap-right {
        right: 0;
    }


    /* This is good for accessibility, so instead use polyfill for :focus-visible
    https://github.com/WICG/focus-visible */
    .touch-tap-left:focus, .touch-tap-right:focus {
        outline: none;
    }

    .left-edge-shape, .right-edge-shape {
        position: absolute;
        fill: white;
        opacity: 0.3;
    }

    .left-edge-shape {
        left: 0;
        transform-origin: left;
    }

    .right-edge-shape {
        right: 0;
        transform-origin: right;
    }

    .red {
        background: rgb(255,6,25);
        background: linear-gradient(145deg, rgba(255,6,25,1) 40%, rgba(255,4,159,1) 100%);
    }

    .orange {
        background: rgb(255,100,6);
        background: linear-gradient(145deg, rgba(255,100,6,1) 40%, rgba(255,183,4,1) 100%);
    }

    .yellow {
        background: rgb(255,241,0);
        background: linear-gradient(145deg, rgba(255,241,0,1) 40%, rgba(239,255,6,1) 100%);
    }

    .green {
        background: rgb(1,159,127);
        background: linear-gradient(145deg, rgba(1,159,127,1) 40%, rgba(161,230,0,1) 100%);
    }

    .blue {
        background: rgb(34,29,233);
        background: linear-gradient(145deg, rgba(34,29,233,1) 40%, rgba(0,206,230,1) 100%);
    }

    .purple {
        background: rgb(114,27,250);
        background: linear-gradient(145deg, rgba(114,27,250,1) 40%, rgba(171,84,250,1) 100%);
    }



    /*

    -------
    .loading {
        position: fixed;
        height: 100%;
        width: 100%;
        left: 0;
        top: 0;
        background: rgba(0, 0, 0, 0.85);
        z-index: 2000;
    }

    .loading span {
        position: absolute;
        font-size: 40px;
        top: 50%;
        left: 50%;
        -webkit-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

    .header button {
        height: 30px;
    }
    
    div.header {
        margin-bottom: 10px;
    }

    table.box td {
        height: 25px;
        width: 25px;

    }
    .pins {
        line-height: 60px
    }

    .pins span {
        padding: 15px;
        cursor: pointer;
    }

    .pins .yes {
        background-color: green
     }

    .pins .no {
        background-color: gray
    }

    .panel-content h1 {
        color: black;
    }

    div.analysisInput {
        height: 200px;
    }

    div.submit {
        height: 100px;
    }

    .pinsInput label {
        color: black;
    }

    .analysisInput label {
        color: black;
        display: block;
        width: 60px;
        margin-left: 10px;
        margin-right: 0px;
        float: left;
        cursor: pointer;
    }

    .analysisInput label.left {
        text-align: right;
        margin-right: 10px;
        margin-left: 0px;
    }

    .analysisInput input {
        display: block;
        width: 70px;
        float: left;
        height: 40px;
    }

    .scoreboard {
        display: block;
        height: 75px;
    }

    .scoreboard .frame {
        float: left;
        margin-right: 30px;
    }
    .scoreboard .score {
        float: left;
    }

    .box {
        border: 1px solid;
    }

    div.flippable {
        background-color: yellow;
        height: 600px;
        width: 140px;
    }

    .collapsed-panel {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }

    .slide-up-panel {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #cccccc;
        border-top: 1px solid #000;
        box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2);
        z-index: 1000;
    }

    .panel-content {
        padding: 0px 20px 20px 40px;
        display: block;
    }

    .slide-up-enter-active,
    .slide-up-leave-active {
        transition: transform 0.3s ease;
    }

    .slide-up-enter,
    .slide-up-leave-to {
        transform: translateY(100%);
    }

    */
</style>

<script setup>
    import { storeToRefs } from 'pinia';
    import { useDisplayStore } from '../stores/display';
    import { useAnalysisStore } from '../stores/analysis';
    import { computed, ref, onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import Hammer from 'hammerjs';

    const displayStore = useDisplayStore();
    const display = storeToRefs(displayStore);

    const analysisStore = useAnalysisStore();
    const analysis = storeToRefs(analysisStore);

    const route = useRoute();

    //onMounted(() => {
    //    const seriesId = route.params.series_id;
    //    displayStore.getSeries(seriesId);
    //});

    onMounted(() => {
        // Set up Hammer element & event listeners to respond to swiping gestures
        const touchContainer = document.getElementById("touch-container");
        const hammer = new Hammer.Manager(touchContainer, {
            recognizers: [
                [Hammer.Pan, { direction: Hammer.DIRECTION_HORIZONTAL }],
                [Hammer.Swipe, { direction: Hammer.DIRECTION_HORIZONTAL }]
            ]
        });
        hammer.on("pan swipe", displayStore.handleTouchEvents);

        // Set up event listeners for when items are transitioning across the screen
        const itemsContainer = document.getElementById("rendered-items-flexbox");

        itemsContainer.addEventListener("transitionstart", (e) => {
            if (e.target === itemsContainer) {
                display.isTransitioning = true;
            }
        });
        itemsContainer.addEventListener("transitionend", (e) => {
            if (e.target === itemsContainer) {
                displayStore.updateCurrentItem();
     	    }
        });

        // For users who prefer reduced motion, can't rely on transition to change items
        displayStore.prefersReducedMotion = window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches;
    });

    console.log('hi');

    /*
    //const frames = display.getMaster.value.gameData[display.getGameNumber.value].frames;
    //const fs = frames.map((e) => e.frameNumber);
    //console.log(fs);
    //.map((e) => e.frameNumber)
    //console.log(`${display.getFrameNumber} :: ${frames}`);
    //console.log(display.getMaster.value.gameData[display.getFrameNumber.value].frames);
    //console.log(display.getGameLeft.value)
    //console.log(display.getFrameLeft.value)
    //console.log(display.getFrameRight.value)

    const togglePanel = () => {
        displayStore.toggleSlider();
    };

    const nextFrame = () => {
        displayStore.nextFrame();
    };

    const prevFrame = () => {
        displayStore.previousFrame();
    };

    const clickPins = (p) => {
        analysisStore.pins(p);
    };
    const pinsClassname = (p) => {
        return analysis.getPinsClicked.value.has(p) ? 'yes' : 'no';
    };
    const spare = () => {
        analysisStore.spare();
    };
    const strike = () => {
        analysisStore.strike();
    };

    const checkMe = () => {
        console.log(display.getAnalysis.value);
    };

    const analysisImages = () => {
        return display.getAnalysis.value;
    };

    const usePins = () => {
        console.log('usingPins');
        analysisStore.usePins();
    };

    const pinsBinding = computed({
        get() {
            return analysisStore.pinsText;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.pinText(value);
        }
    });

    const pinExitBinding = computed({
        get() {
            return analysisStore.pinExit;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(1, parseInt(value));
        }
    });

    const pinEnterBinding = computed({
        get() {
            return analysisStore.pinEnter;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(2, parseInt(value));
        }
    });

    const breakPointBinding = computed({
        get() {
            return analysisStore.breakPoint;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(3, parseInt(value));
        }
    });

    const breakDistanceBinding = computed({
        get() {
            return analysisStore.breakDistance;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(4, parseInt(value));
        }
    });

    const arrowsBinding = computed({
        get() {
            return analysisStore.arrows;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(5, parseInt(value));
        }
    });

    const slideBinding = computed({
        get() {
            return analysisStore.slide;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(6, parseInt(value));
        }
    });

    const startDotsBinding = computed({
        get() {
            return analysisStore.startDots;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(7, parseInt(value));
        }
    });

    const startDistanceBinding = computed({
        get() {
            return analysisStore.startDistance;
        },
        set(value) {
            console.log(`setting...${value}`);
            analysisStore.setAnalysis(8, parseInt(value));
        }
    });

    const submitThrow = () => {

        let payload = {};
        payload['series_id'] = route.params.series_id;
        payload['game_number'] = display.gameNumber.value;

        //console.log(display.usePins);

        if (!display.usePins) {
            payload['throw'] = analysis.pinsText.value;
        }
        
        if (analysis.anyAnalysis.value) {
            payload['data'] = {};

            if (display.usePins) {
                payload['data']['pins'] = [...analysis.getPinsActive.value];
            }
            else {

                //console.log(typeof pinsBinding.value);

                if (['X', '/'].includes(pinsBinding.value)) {
                    payload['data']['pins'] = pinsBinding.value;
                }
                else {
                    payload['data']['pins'] = [...analysis.pinsClick.value];
                }
            }
            delete payload['throw']
        }
   
        if (analysis.pexOn.value) {
            //console.log(analysis.pexOn);
            //console.log(analysis.pexOn.value);

            payload['data']['pin_exit'] = analysis.pinExit.value;
        }
        if (analysis.penOn.value) {
            payload['data']['pin_entry'] = analysis.pinEnter.value;
        }
        if (analysis.breakPtOn.value) {
            payload['data']['break_point'] = analysis.breakPoint.value;
        }
        if (analysis.breakDistOn.value) {
            payload['data']['break_distance'] = analysis.breakDistance.value;
        }
        if (analysis.arrowsOn.value) {
            payload['data']['arrows'] = analysis.arrows.value;
        }
        if (analysis.slideOn.value) {
            payload['data']['slide'] = analysis.slide.value;
        }
        if (analysis.startDotsOn.value) {
            payload['data']['start'] = analysis.startDots.value;
        }
        if (analysis.startDistOn.value) {
            payload['data']['start_distance'] = -1 * Math.abs(analysis.startDistance.value);
        }

        console.log(JSON.stringify(payload));

    };

    const toggleAnalysis = (i) => {
        
        console.log(i);
        analysisStore.toggleAnalysis(i);
    };

    const leftFrameDisabled = computed({
        get() {
            return display.getFrameNumber.value === 1
        }
    });
    const rightFrameDisabled = computed({
        get() {
            return display.getFrameNumber.value === Math.max(...display.getTotalFrames.value);
        }
    });
    */

</script>
