'use strict';
app.factory('PollService',
            ['httpService', '$location','constants','$q','$window', '$rootScope', '$auth', 'AuthService', 
            function(httpService,$location,constants,$q,$window, $rootScope, $auth, AuthService){

            	var createPoll = function(disaster_name, disaster_description, disaster_type, disaster_city, disaster_lat, disaster_long){
            		var url = constants['API_SERVER']+'disaster/sys/disaster/';
            		var deferred = $q.defer()
            		httpService.httpPost(url, {
            			'disaster_name':disaster_name,
                              'disaster_description':disaster_description,
                              'disaster_type':disaster_type,
                              'disaster_city':disaster_city,
                              'disaster_lat':disaster_lat,
                              'disaster_long':disaster_long
            		}).then(function(response){
            			deferred.resolve(response);
            			//success post

            		},function(response){
            			//error post
            			deferred.reject(response);

            		});

            		return deferred.promise;

            	};

            	var createChoice = function(qid, choice_text){
            		var url = constants['API_SERVER']+'polls/sys/choice/';
            		var deferred = $q.defer()
            		httpService.httpPost(url, {
            			'qid':qid,
            			'choice_text':choice_text
            		}).then(function(response){
            			deferred.resolve(response);
            			//success post

            		},function(response){
            			//error post
            			deferred.reject(response);

            		});

            		return deferred.promise;

            	};

            	var getQues = function(id){

            		var url = constants['API_SERVER']+'polls/sys/question/'+id+'/';
            		var deferred = $q.defer();
            		httpService.httpGet(url).then(function(response){
            			deferred.resolve(response);
            			//success post

            		},function(response){
            			//error post
            			deferred.reject(response);

            		});

            		return deferred.promise;

            	};

            	var getIndexList = function(){
            		var url = constants['API_SERVER']+'disaster/sys/disaster/';
            		var deferred = $q.defer();
            		httpService.httpGet(url).then(function(response){
            			deferred.resolve(response);
            			//success post

            		},function(response){
            			//error post
            			deferred.reject(response);

            		});

            		return deferred.promise;

            	};

                  

                  var vote = function(cid, qid){

                        var url = constants['API_SERVER']+'polls/vote/';
                        var deferred = $q.defer();
                        httpService.httpPost(url, {
                              'cid':cid,
                              'qid':qid
                        }).then(function(response){
                              deferred.resolve(response);
                              //success post

                        },function(response){
                              //error post
                              deferred.reject(response);

                        });

                        return deferred.promise;

                  };

            	return{

            		createQues : function(disaster_name, disaster_description, disaster_type, disaster_city, disaster_lat, disaster_long ){
            			return createPoll(disaster_name, disaster_description, disaster_type, disaster_city, disaster_lat, disaster_long);
            		},
            		createChoice : function(qid, choice_text){
            			return createChoice(qid, choice_text);
            		},
            		getQues : function(id){
            			return getQues(id);
            		},
            		getIndexView : function(){
            			return getIndexList();
            		},
                        vote: function(cid, qid){
                              return vote(cid,qid);
                        }


            	};

            }]);
   