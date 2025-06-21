import { ref, computed, toRaw } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { _ } from 'lodash';

export const useDisplayStore = defineStore('display', {

    state: () => {


        return {
            loading: ref(true),
            items: ["red", "orange", "yellow", "green", "blue", "purple"], // IDs for all items
            isInfiniteLoop: false, // Whether to loop back to start of item array when reaching the end
            prefersReducedMotion: false,
            currentIndex: 0,
            upcomingIndex: 0,
            translateX: 0,
            maxTranslateX: 0,
            transformStyle: "translateX(0)",
            transitionClass: "transition-initial",
            isTransitioning: false,
            leftEdgeScale: 0,
            rightEdgeScale: 0
        };

        /*
        return {
            loading: ref(true),
            sliderOpen: ref(false),

            gameNumber: 1,
            frameNumber: 1,
            analysisCursor: ref(0),
            master: ref({
                games: [1,2,3],
                gameData: {
                    "1": {
                        "frames": [
                            {
                                "frame": "1",
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "7"
                                    },
                                    {
                                        "pins": "/"
                                    }
                                ],
                                "total": 18
                            },
                            {
                                "frame": "2",
                                "throws": [
                                    {
                                        "id": "a",
                                        "pins": "8"
                                    },
                                    {
                                        "pins": "1"
                                    }
                                ],
                                "total": 27
                            },
                            {
                                "frame": "3",
                                "throws": [
                                    {
                                        "id": "b",
                                        "pins": "X"
                                    },
                                ],
                                "totalScore": ""
                            },
                        ],
                        "analysis": {
                            "a": {
                                "url": "https://dbeusqqg6817d.cloudfront.net/muskiemania/abc123_1_7c314aca36b2.png"
                            },
                            "b": {
                                "url": "https://dbeusqqg6817d.cloudfront.net/muskiemania/xyz123_1_7e6976d9bebe.png"
                            }
                        }
                    },
                    "2": {
                    },
                    "3": {
                    }
                }
            })
        };

        */
    },
    getters: {

        infoItems: (state) => {
            let arr = [...state.items];
            // If there are only 2 items, double array to anways have odd numbre in renderedItems
            if (arr.length === 2) {
                arr = [...arr, ...arr];
            }

            return arr.map((id, index) => ({
                id,
                key: `${id}-${index}`
            }));
        },

        renderedItems: (state) => {
            const { currentIndex: i, infoItems } = state;
            
            if (infoItems.length === 1) {
                return [infoItems[0]];
            }

            const lastIndex = infoItems.length - 1;
            const prevIndex = i === 0 ? lastIndex : i - 1;
            const nextIndex = i === lastIndex ? 0 : i + 1;

            return [infoItems[prevIndex], infoItems[i], infoItems[nextIndex]];
        },

        isNextAvailable: (state) => {
            const { items, currentIndex, isInfiniteLoop } = state;
            return (
                currentIndex < items.length - 1 ||
                (isInfiniteLoop && items.length !== 1)
            );
        },

        isPreviousAvailable: (state) => {
            const { items, currentIndex, isInfiniteLoop } = state;
            return currentIndex > 0 || (isInfiniteLoop && items.length !== 1);
        },
        
        /*

        isLoading: (state) => state.loading,
        getGameNumber: (state) => state.gameNumber,
        getGameLeft: (state) => state.gameNumber > 1,
        getGameRight: (state) => state.gameNumber === Math.max(state.master.games),
        getFrameNumber: (state) => state.frameNumber,
        getTotalFrames: (state) => {
            let total = [];
            try {
                total = state.master.gameData[state.gameNumber.toString()].frames.map((e) => e.frame);
            } catch (error) {
                total = [];
            } finally {
                return total;
            }
        },
        getFrameThrows: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames;
            const fr = f.find((e) => e.frame === state.frameNumber.toString());
            console.log(state.frameNumber);
            console.log(fr);

            return fr['throws'].map((e) => e['pins']);
        },
        getFrameScore: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frame === state.frameNumber.toString());
            return f.total
        },
        getSliderIsOpen: (state) => state.sliderOpen,
        getAnalysis: (state) => {
            const f = state.master.gameData[state.gameNumber.toString()].frames.find((e) => e.frame === state.frameNumber.toString());
            const t = f['throws'].map((e) => e['id']).filter(value => value !== undefined);

            //return toRaw(f);

            let u = [];
            t.forEach((i) => {
                const a = state.master.gameData[state.gameNumber.toString()].analysis || {};
                if (i in a) {
                    u.push(a[i].url)
                }
            });
            return u;
        },
        getMaster: (state) => state.master

        */
    },
    actions: {
        
        handleTouchEvents(e) {
            const {
                isTransitioning,
                translateX,
                leftEdgeScale,
                rightEdgeScale,
                isPreviousAvailable,
                isNextAvailable
            } = this;
            const { deltaX, deltaY, isFinal } = e;

            // While card is transitioning, don't respond to events
            if (isTransitioning) {
                return;
            }

            // Don't respond to gestures that are more vertical than horizontal
            // (browser will handle vertical scroll)
            // Unless the gesture started horizontal, then respond as normal
            if (
                (Math.abs(deltaX) < 8 || 
                    Math.abs(deltaY) - Math.abs(deltaX) > -1) &&
                !translateX &&
                !leftEdgeScale &&
                !rightEdgeScale) {
                return;
            }

            if (
                (!isPreviousAvailable && deltaX > 0) ||
                (!isNextAvailable && deltaX < 0)
            ) {
                this.updateEdgeEffect(deltaX, isFinal);
            } else if (isFinal) {
                this.handleGestureEnd(deltaX);
            } else {
                this.handleGestureMove(deltaX);
            }
        },

        handleGestureMove(deltaX) {
            const { maxTranslateX } = this;

            // Record farthest distance in one direction so can check if gesture goes in
            // opposite direction, indicating user doesn't want to change slides
            if (Math.abs(deltaX) > Math.abs(maxTranslateX)) {
                this.maxTranslateX = deltaX;
            }

            // Move items by deltaX amount
            this.translateX = deltaX;
            this.transitionClass = "transition-initial";
            this.transformStyle = `translateX(${deltaX}px)`;
        },

        handleGestureEnd() {
            const { translateX, maxTranslateX } = this;

            if (Math.abs(translateX) - Math.abs(maxTranslateX) < -1) {
                // If gesture goes too much in oposite direction, stay on current slide
                this.transitionClass = 'transition-item';
                this.transformStyle = 'translateX(0)';
            } else if (translateX > 0) {
                this.previous();
            } else if (translateX < 0) {
                this.next();
            }
        },

        updateEdgeEffect(deltaX = 0, isFinal = false) {
            if (isFinal) {
                this.transitionClass = "transition-edge";
                this.leftEdgeScale = 0;
                this.rightEdgeScale = 0;
            } else {
                this.transitionClass = "transition-initial";
                const scaleVal = Math.min(0.2 + Math.abs(deltaX) / 50, 1);
                if (deltaX > 0) {
                    this.leftEdgeScale = scaleVal;
                }
                if (deltaX < 0) {
                    this.rightEdgeScale = scaleVal;
                }
            }
        },

        // Debounce previous & next functions so only triggered by individual gestures
        previous: _.debounce(
            function() {
                if (this.isTransitioning) {
                    return;
                }

                if (!this.isPreviousAvailable) {
                    this.updateEdgeEffect(100, false);
                    setTimeout(() => {
                        this.updateEdgeEffect(0, true);
                    }, 100);
                    return;
                }

                const { currentIndex, items, prefersReducedMotion } = this;

                this.transitionClass = "transition-item";
                this.transformStyle = "translateX(100vw)";

                const prevIndex =
                    currentIndex === 0 ? items.length - 1 : currentIndex - 1;
                this.upcomingIndex = prevIndex;

                if (prefersReducedMotion) {
                    this.updateCurrentItem();
                }
            },
            100,
            { leading: true, trailing: false }
        ),

        // Respond to "next" navigation request
        // Figure out which card is next and call updateCurrentItem
        next: _.debounce(
            function() {
                if (this.isTransitioning) {
                    return;
                }

                if (!this.isNextAvailable) {
                    this.updateEdgeEffect(-100, false);
                    setTimeout(() => {
                        this.updateEdgeEffect(0, true);
                    }, 100);
                    return;
                }

                const { currentIndex, items, prefersReducedMotion } = this;

                this.transitionClass = "transition-item";
                this.transformStyle = "translateX(-100vw)";

                const nextIndex =
                    currentIndex === items.length - 1 ? 0 : currentIndex + 1;
                this.upcomingIndex = nextIndex;

                if (prefersReducedMotion) {
                    this.updateCurrentItem();
                }
            },
            100,
            { leading: true, trailing: false }
        ),

        // If using Vue Router or Vuex, can put that logic here instead of just changing local state
        updateCurrentItem() {
            this.currentIndex = this.upcomingIndex;
            this.resetTranslate();
        },

        resetTranslate() {
            this.isTransitioning = false;
            this.transitionClass = "transition-initial";
            this.transformStyle = "translateX(0)";
            this.translateX = 0;
            this.maxTranslateX = 0;
        },

        /*

        toggleSlider() {
            this.sliderOpen = !this.sliderOpen            
        },
        nextFrame() {
            this.frameNumber++
        },
        previousFrame() {
            this.frameNumber--
        },

        */
        getSeries(seriesId) {
            
            const BASE_URL = 'https://smqu6xcne4.execute-api.us-west-2.amazonaws.com';

            // must call out to API to retrieve series
            // then initialize
            // finally set loading ==> false
            axios.get(`${BASE_URL}/series/${seriesId}`)
            .then((reply) => {
               
                console.log(reply);
                this.loading = false;

                /*

                const master = {};
                master.games = reply.data.games;
                master.gameData = reply.data.game_data;

                const current = Math.max(...reply.data.games)

                let frames = [];
                try {
                    frames = master.gameData[current.toString()].frames.map((e) => e.frame);
                } catch (error) {
                    
                }
                
                const thisFrame = Math.max(...frames);

                this.master = master;
                this.frameNumber = parseInt(thisFrame);
                this.gameNumber = parseInt(current);
                this.loading = false;
                */
            })
            .catch((error) => {
                console.log(error);
            });

        }
    }
});

