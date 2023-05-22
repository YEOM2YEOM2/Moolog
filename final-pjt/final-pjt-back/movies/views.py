from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import NowPlayingMovieSerializer, NowPlayingMovieListSerializer, NowPlayingMovieReviewSerializer
from .serializers import UpcomingMovieSerializer, UpcomingMovieListSerializer, UpcomingMovieReviewSerializer
from .serializers import PopularMovieSerializer, PopularMovieListSerializer, PopularMovieReviewSerializer
from .models import NowPlayingMovie, NowPlayingReview, UpcomingMovie, UpcomingReview, PopularMovie, PopularReview

# Create your views here.
@api_view(['GET'])
def now_playing_movie_list(request):
    movies = get_list_or_404(NowPlayingMovie)
    serializer = NowPlayingMovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing_movie_detail(request, movie_id):
    movie = get_object_or_404(NowPlayingMovie, pk=movie_id)
    serializer = NowPlayingMovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing_movie_review_list(request):
    reviews = get_list_or_404(NowPlayingReview)
    serializer = NowPlayingMovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 현재 상영작 리뷰 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def now_playing_movie_review_detail(request, review_pk):
    review = get_object_or_404(NowPlayingReview, pk=review_pk)

    if request.method == 'GET':
        serializer = NowPlayingMovieReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = NowPlayingMovieReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 현재 상영작 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def now_playing_movie_review_create(request, movie_id):
    movie = get_object_or_404(NowPlayingMovie, pk=movie_id)
    serializer = NowPlayingMovieReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 현재 상영작 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def now_playing_movies_likes(request, movie_id):
    movie = get_object_or_404(NowPlayingMovie, pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    
    serializer = NowPlayingMovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

# 개봉 예정작
@api_view(['GET'])
def upcoming_movie_list(request):
    movies = get_list_or_404(UpcomingMovie)
    serializer = UpcomingMovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def upcoming_movie_detail(request, movie_id):
    movie = get_object_or_404(UpcomingMovie, pk=movie_id)
    serializer = UpcomingMovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def upcoming_movie_review_list(request):
    reviews = get_list_or_404(UpcomingReview)
    serializer = UpcomingMovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 개봉 예정작 리뷰 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def upcoming_movie_review_detail(request, review_pk):
    review = get_object_or_404(UpcomingReview, pk=review_pk)

    if request.method == 'GET':
        serializer = UpcomingMovieReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = UpcomingMovieReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 개봉 예정작 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upcoming_movie_review_create(request, movie_id):
    movie = get_object_or_404(UpcomingMovie, pk=movie_id)
    serializer = UpcomingMovieReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 개봉 예정작 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upcoming_movies_likes(request, movie_id):
    movie = get_object_or_404(UpcomingMovie, pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    
    serializer = UpcomingMovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

# 인기 영화
@api_view(['GET'])
def popular_movie_list(request):
    movies = get_list_or_404(PopularMovie)
    serializer = PopularMovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def popular_movie_detail(request, movie_id):
    movie = get_object_or_404(PopularMovie, pk=movie_id)
    serializer = PopularMovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def popular_movie_review_list(request):
    reviews = get_list_or_404(PopularReview)
    serializer = PopularMovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 인기 영화 리뷰 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def popular_movie_review_detail(request, review_pk):
    review = get_object_or_404(PopularReview, pk=review_pk)

    if request.method == 'GET':
        serializer = PopularMovieReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PopularMovieReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 인기 영화 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def popular_movie_review_create(request, movie_id):
    movie = get_object_or_404(PopularMovie, pk=movie_id)
    serializer = PopularMovieReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 인기영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def popular_movies_likes(request, movie_id):
    movie = get_object_or_404(PopularMovie, pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    
    serializer = PopularMovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)