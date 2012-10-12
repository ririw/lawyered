import sqlite3
import wpScraper
import sys
import httplib
import logging
import urllib
import json
import logging
import pandas
logging.basicConfig(filename='scraper.log',level=logging.INFO)
logger = logging.root
logger.addHandler(logging.StreamHandler())

import argparse

parser = argparse.ArgumentParser(
   description="Scrape a wordpress site")
parser.add_argument(
      'wpid',
      metavar = 'wordpressID',
      type=int,
      help="The ID of the wordpress blog to scrape")
parser.add_argument(
      '-u',
      type=str,
      help="A file with a comma separated list of users who lie " + 
         "if this is omitted, the system will output the list as if "+
         "everyone's truthfullness is unknown"
      )
parser.add_argument(
      '-s',
      type=str,
      help="The file in which to store the results. If unspecified, this will "+
           "go to stdout."
      )


def scrapeGame(wpID):
   gameConnection = httplib.HTTPSConnection('public-api.wordpress.com')
   gameConnection.request('GET', '/rest/v1/sites/%d/posts/' % wpID)
   postsConn = gameConnection.getresponse()
   #postsJSON = postsConn.read()
   postsJSON = json.loads(postsConn.read())
   postIDs = []
   posts = {}
   for post in postsJSON['posts']:
      postIDs.append(post['ID'])
      posts[post['ID']] = post['title']
   logging.info("Got posts %s" % postIDs)
   comments = []
   for postID in postIDs:
      gameConnection.request(
            'GET', 
            '/rest/v1/sites/%d/posts/%d/replies?number=100' % (wpID, postID))
      logging.info("Getting replies to post %d:%s" % (postID, posts[postID]))
      commentsConn = gameConnection.getresponse()
      commentsJSON = json.loads(commentsConn.read())
      totalComments = commentsJSON['found']
      commentsRead = 100
      while totalComments > 0:
         newComments = map(lambda c: 
                  (c['ID'], c['author']['name'], c['content']), 
                  commentsJSON['comments'])
         comments.extend(newComments)

         gameConnection.request(
               'GET', 
               '/rest/v1/sites/%d/posts/%d/replies?offset=%d&number=100' % (wpID, postID, commentsRead))
         logging.info("Getting replies to post %d with offset %d" % 
               (postID, commentsRead))
         commentsConn = gameConnection.getresponse()
         commentsJSON = json.loads(commentsConn.read())
         totalComments -= len(newComments)
         commentsRead += len(newComments)
   ids = []
   posts = []
   contents = []
   authors = []
   for comment in comments:
      ids.append(comment[0])
      authors.append(comment[1])
      contents.append(comment[2])
      posts.append(postID)
   return pandas.DataFrame({
      'id':ids, 
      'post':posts,
      'content':contents,
      'author':authors})
if __name__=="__main__":
   args = parser.parse_args()
   liarSet = None
   targetFile = sys.stdout
   if args.s:
      targetFile = file(args.s, 'w')
   if args.u:
      liarSet = set()
      with file(args.u) as liars:
         # replace newlines with commas and split at commas, then remove 
         # whitespace.
         liarSet = liarSet.union(
               map(str.strip, liars.read().replace("\n", ",").split(",")))
   game = wpScraper.scrapeGame(args.wpid)
   game['asciiContent'] = map(lambda a: a.encode('ascii', 'ignore'),
         game['content'])
   if liarSet:
      game['truth'] = map(lambda u: not (u in liarSet), game['author'])
      game[['asciiContent', 'truth']].to_csv(targetFile, index=False, header=False)
   else:
      game['truth'] = map(lambda u: "unknown", game['author'])
      game[['asciiContent', 'truth']].to_csv(targetFile, index=False, header=False)
