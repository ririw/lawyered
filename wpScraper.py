import httplib
import urllib
import json
import logging
import pandas

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
