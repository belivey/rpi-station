<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use League\Flysystem\Filesystem;
use League\Flysystem\Adapter\Ftp as Adapter;

class ftpClient extends Model
{
    protected $guarded = [];

    public static function upload(){
      foreach (ftpClient::all() as $client){
        $station_id = $client->station_id
          ?$client->station_id
          :Configuration::find(1)->station_id;

        $filesystem = new Filesystem(new Adapter([
            'host' => $client->host,
            'username' => $client->login,
            'password' => $client->password,

            'port' => 21,
            'root' => $client->directory,
            'passive' => true,
            // 'ssl' => true,
            'timeout' => 30,
        ]));

        foreach(StationData::unsent($client) as $data){
            if ($filesystem->put(
                $station_id."_".date("YmdHis", strtotime($data->measured_at)).".json",
                json_encode([
                  "measured_at" => date("Y-m-d H:i:s", strtotime($data->measured_at)),
                  "st_index" => $station_id,
                  "data" => $data->data,
                ])
              ))
            {
              $client->update([
                'last_sent_data_id' => $data->id
              ]);
            } else {
              return false;
            }
        }

        return true;
      }

    }
}