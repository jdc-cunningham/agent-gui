### 03/24/2026

7:27 PM

I really need to wrap this project up, I have other things to do, I keep getting farther away from my original interest in this project too so losing drive

Tonight I think I want to:

- [ ] render the agents on left side
- [ ] render agents on right side
- [ ] agent actualy runs
- [ ] agent can take commands from input box

That may be too much I have like 1.5 hrs

7:47 PM

Ugh... for scrollbars need to turn it into a canvas

### 03/21/2026

9:08 AM

Well I've got like 3 hrs to work on this

I want to wrap this project up today, this agent harness/client thing I'll keep adding stuff to over time if it sticks as something I usage

I mentioned in the video that it's been a while since I started this project, I ordered the first laptop 03/03/2026 and yeah... losing momentum/interest

Still have a ways to go from a usable interface

I'm repeating these but I'll just type them out

- [x] make a popup modal that can add agents
 - [x] make modal
 - [x] add button opens modal
 - [x] create agent detail inputs eg. model, prompt, tools
 - [x] inserts agent into sqlite db
  - has no dupe or error checking
- [ ] show agents on left side bar
 - [x] get list of agents
 - [ ] clicking an agent runs it
- [ ] run agent
 - [ ] agent runs in its own thread
 - [ ] agent has its own pane, scrollable
 - [ ] can close agents

I am a little distracted today's gonna be fun, first time I fly the Vortex 3 DLG in months and then doing some more photography at new locations

Let me get my coffee and music going

9:49 AM

Making progress, it's so like slow to work on this tiny laptop and my neck. looking down at it

I have an external monitor that I'm using a 22" 1080P screen that helps but still I can feel my neck aching as I'm looking down at these monitors and this keyboard on the ASUS EEE 1005HA PC squeaks as you type

(insert picture here)

10:34 AM

Alright at this point I've got a modal that has the fields

I don't have the save to DB mechanism implemented yet but I've got the show/hide modal part

11:00 AM

I'm going to stop, I want to prep for my day out but made good progress, I'll return to this tonight

---

### 03/19/2026

8:32 PM

I've been writing some code on this finally, was screwing around with ordering 2 of these ASUS 1005HA laptops, I ordered one as parts, was listed no OS... was like fine. But turns out the screen is broken so I ordered another one... that one had its own problems like a loud fan. So I had to disassemble both of them to swap displays and upgrade to an SSD. I also upgraded the ram to 2GB from the 2nd laptop with the non-broken display.

Anyway I'm writing this devlog/this app on this laptop now. With the white 3D-printed hite bezel cover to make the laptop look entirely white like the ASUS EEE PC 1000.

I've got a left-right panel setup right now in my desktop window

Need to setup:

- [ ] sqlite
- [ ] add button on left panel
- [ ] agent settings
- [ ] list the agents on the left panel, scrolls
- [ ] run the agents as threads
- [ ] show the agent output in the right as separate containers, right panel scrolls

10:14 PM

Made progress, have two panels

Started the DB, still need to actually have it linked together

Make agents, run them... guess I'll be working on this over the weekend too

---

### 03/11/2026

8:39 PM

Here we go... another project

Kate is looking good memory usage wise, I have 1GB on this ASUS EEE 1005HA right now so it's at 239M/989M usage as I type this into Kate.

Got this spacious 1920x1080P compared to the 1024x600 laptop screen which is also broken (huge black area on the LCD screen). The second laptop I ordered is fully functional with 2GB of RAM, same model as this one, I may need to get an SSD though before I do this process again of putting Debina XFCE on this laptop. It took like 2 hrs to install but can't complain, pretty amazing to load up Linux on a 17 year old laptop and it just works. Or netbook I should say.

Okay so I'm about to eat dinner in 15 minutes but first thing will be to do some preliminary checks.

- [x] get a Tkinter window opened on this laptop from Python
- [ ] compile it so it runs as an so file
- [ ] add some LLM model API keys and get first langchain agent running
- [ ] come up with an initial UI and build it
- [ ] come up with workflows
  - [ ] pull down Hacker News
  - [ ] get regular news
  - [ ] my finances eg. balances from a local DB
  - [ ] weather
- [ ] dark mode with neon colors

Eventually I actually want things like satellite imagery analysis, grain futures, stocks, etc..

6:53 PM
So I do have to install tkinter eg. `sudo apt install python-tk`

9:55 PM

I'm pretty spent now but will make something basic like this

<img src="./devlog-images/basic-ui.JPG"/>

Then will use agents with their own threads
