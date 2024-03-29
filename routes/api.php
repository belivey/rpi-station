<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/door/{status}', 'DoorController@doorStatus');
Route::get('/door', 'DoorController@index');
Route::get('/power', 'AlertController@power');
Route::get('/ui', 'ConfigurationController@ui');

Route::get('/lastdata/{ndays}', 'StationDataController@lastData');
Route::get('/history', 'StationDataController@history');

Route::get('/alerts', 'AlertController@index');
