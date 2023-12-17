import discord
import requests
import base64
import json
from discord.ext import commands

# refer to https://www.oit.ac.jp/rd/labs/kobayashi-lab/~yagshi/new/_book/spotify_python.html

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spotify(self, ctx, *, artist: str = None):
        if artist is None:
            await ctx.send("format: /spotify <artist>")
            return

        client_id = ' < set your client id > ' 
        client_secret = ' < set your client secret > '
        auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode('utf-8')
        headers = {'Authorization': f"Basic {auth_header}"}
        data = {'grant_type': 'client_credentials'}
        resp0 = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

        if resp0.status_code == 200:
            resp = resp0.json()
            token = resp.get('access_token')
        else:
            await ctx.send("failure get access token")
        
        head = {
            'Authorization': 'Bearer ' + token 
        }

        SPOTIFY_API_URL = 'https://api.spotify.com/v1/search'
        params = {'q': artist, 'type': 'artist'}
 
        response = requests.get(SPOTIFY_API_URL, headers=head, params=params)

        if response.status_code == 200:
            data = response.json()

            if data['artists']['items']:
                artist_info = data['artists']['items'][0]
                await ctx.send(f"Artist: {artist_info['name']}\nFollowers: {artist_info['followers']['total']}\nGenres: {', '.join(artist_info['genres'])}")
            else:
                await ctx.send("No data")
        else:
            await ctx.send("Unable to data from Spotify API")

async def setup(bot):
    await bot.add_cog(Spotify(bot))