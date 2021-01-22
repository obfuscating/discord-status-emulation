# discord status emulation

> "how get purple status"
#### i am done hearing this
#### now u can do it for urself and get epic purple status plus more

## requirements:
* a brain
* maybe basic python knowledge

### you need to get your `token` from discord before you can run this

# steps:
## 1. getting your token
#### there's 2 ways to get your discord token
1. `discord.com web client`
2. `discord desktop client`

#### we can go over both ways and their steps

# web client
1. go to discord.com and sign into your account if you aren't already
2. press `ctrl + shift + i` on your keyboard to open `Developer Tools/Inspect Element` OR click the 3 dots/bars on the top right and go to `More Tools > Developer Tools`
3. inside the `Developer Tools`, find the `Application` tab (it may be hidden. you can find it by pressing the two arrows `(>>)` and hit `Application`)
4. inside `Application`, open the `Local Storage` tree and then click on `https://discord.com`
5. scroll all the way down inside the list until you reach the bottom where you will be greeted with some blank space
6. (you need to be quick for this part) refresh the page until you see a new entry appear in the list called `token`. on the right a jumble of text will appear and you'll need to double click then hit `ctrl + c` on your keyboard to copy the token

# desktop client
#### this process is relatively similar but is a little bit more of a pain to do
1. inside your desktop client, press `ctrl + shift + i` to open `Developer Tools/Inspect Element`
2. go to the `Application` tab and then open the `Local Storage` tree and go into `https://discord.com`
3. scroll all the way down until you reach the bottom
4. (this is the annoying part) press `ctrl + r` on your keyboard to restart your Discord instance and then quickly copy the token

#### now that you have your token, we can move onto the code part

## 2. running the code
### assuming you already have the python file downloaded, follow these steps
1. open the `.py` file with whatever text editor/IDE you prefer
2. go to the very last line and replace `"your token"` with the token you copied earlier
3. choose which status you'd like to display (`Playing`, `Watching`, `Listening`, `Streaming`) by uncommenting it (delete the `#` right before it)
4. run the file

## 😎 profit
