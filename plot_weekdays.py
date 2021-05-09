import datetime as dat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

month = r"alltime"
lookback_from = '01/01/2021' #MM/DD/YYYY

def memberflow():
    frame = "_memberflow.csv"
    f = month + frame
    df = pd.read_csv(f, header=0)
    df["DateTime"] = pd.to_datetime(df.DateTime)
    df["Weekday"] = df.DateTime.dt.day_name()
    df["Day"] = df["DateTime"].dt.day
    df["Month"] = df.DateTime.dt.month_name()
    df["Year"] = df["DateTime"].dt.year
    dfn = df.loc[df.DateTime >= lookback_from, :]
    weekdays = ['Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday']
    
    ### Plot data by WEEKDAY.
    wd = df[['Total Members', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index()
    wds = df[['Total Members', 'Weekday']].groupby('Weekday').std().reindex(weekdays).reset_index()
    wdn = dfn[['Total Members', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index()
    wdns = dfn[['Total Members', 'Weekday']].groupby('Weekday').std().reindex(weekdays).reset_index()

    fig, (ax1,ax2) = plt.subplots(nrows=2, figsize=(8,7))
    ax1.barh(wd['Weekday'], wd['Total Members'], xerr=wds['Total Members'], align='center')
    ax2.barh(wdn['Weekday'], wdn['Total Members'], xerr=wdns['Total Members'], align='center')
    plt.suptitle('Average Weekday Member Count at The Gate', fontsize=14)
    ax1.set_title("YTD Data: Comprehensive", fontsize=8)
    string = "YTD From: "
    ax2_title = string+lookback_from
    ax2.set_title(ax2_title, fontsize=8)
    plt.xlabel("Total Members")

    xmin1 = min(wd['Total Members']) - max(wds['Total Members']) - 100
    xmin2 = min(wdn['Total Members']) - max(wdns['Total Members']) - 100
    xmax1 = max(wd['Total Members']) + max(wds['Total Members']) + 100
    xmax2 = max(wdn['Total Members']) + max(wdns['Total Members']) + 100
    ax1.set_xlim(xmin1, xmax1)
    ax2.set_xlim(xmin2, xmax2)

    plt.savefig('memberflow_weekday_all.png', dpi=300)
    
memberflow()



def messages():
    frame = "_messages.csv"
    f = month + frame
    df = pd.read_csv(f, header=0)
    df["DateTime"] = pd.to_datetime(df.DateTime)
    df["Weekday"] = df.DateTime.dt.day_name()
    df["Day"] = df["DateTime"].dt.day
    df["Month"] = df.DateTime.dt.month_name()
    df["Year"] = df["DateTime"].dt.year
    dfn = df.loc[df.DateTime >= lookback_from, :]
    weekdays = ['Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday']

    ### Plot data by WEEKDAY.
    wd = df[['Messages', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index()
    wdn = dfn[['Messages', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index()

    fig, (ax1,ax2) = plt.subplots(nrows=2, figsize=(8,7))
    ax1.barh(wd['Weekday'], wd['Messages'], align='center')
    ax2.barh(wdn['Weekday'], wdn['Messages'], align='center')
    plt.suptitle('Average Weekday Messages Sent at The Gate', fontsize=14)
    ax1.set_title("YTD Data: Comprehensive", fontsize=8)
    string = "YTD From: "
    ax2_title = string+lookback_from
    ax2.set_title(ax2_title, fontsize=8)
    plt.xlabel("Messages Sent")

    xmin1 = min(wd['Messages']) - 10
    xmin2 = min(wdn['Messages']) - 10
    xmax1 = max(wd['Messages']) + 10
    xmax2 = max(wdn['Messages'])+ 10
    ax1.set_xlim(xmin1, xmax1)
    ax2.set_xlim(xmin2, xmax2)

    plt.savefig('message_weekday_all.png', dpi=300)

messages()



def voice():
    frame = "_voice.csv"
    f = month + frame
    df = pd.read_csv(f, header=0)
    df["DateTime"] = pd.to_datetime(df.DateTime)
    df["Weekday"] = df.DateTime.dt.day_name()
    df["Day"] = df["DateTime"].dt.day
    df["Month"] = df.DateTime.dt.month_name()
    df["Year"] = df["DateTime"].dt.year
    dfn = df.loc[df.DateTime >= lookback_from, :]
    weekdays = ['Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday', 'Saturday', 'Friday']
    
    ### Plot data by WEEKDAY.
    wd = df[['Minutes', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index()
    wds = df[['Minutes', 'Weekday']].groupby('Weekday').std().reindex(weekdays).reset_index()
    wdn = dfn[['Minutes', 'Weekday']].groupby('Weekday').mean().reindex(weekdays).reset_index() 
    wdns = dfn[['Minutes', 'Weekday']].groupby('Weekday').std().reindex(weekdays).reset_index()
    
    fig, (ax1,ax2) = plt.subplots(nrows=2, figsize=(8,7))
    ax1.barh(wd['Weekday'], wd['Minutes'], xerr=wds['Minutes'], align='center') 
    ax2.barh(wdn['Weekday'], wdn['Minutes'], xerr=wdns['Minutes'], align='center')
    plt.suptitle('Average Weekday Voice Minutes at The Gate', fontsize=14) 
    ax1.set_title("YTD Data: Comprehensive", fontsize=8)
    string = "YTD From: "
    ax2_title = string+lookback_from
    ax2.set_title(ax2_title, fontsize=8)
    plt.xlabel("Voice Minutes")

    xmin1 = min(wd['Minutes']) - max(wds['Minutes']) - 100
    xmin2 = min(wdn['Minutes']) - max(wdns['Minutes']) - 100
    xmax1 = max(wd['Minutes']) + max(wds['Minutes']) + 100
    xmax2 = max(wdn['Minutes']) + max(wdns['Minutes']) + 100
    ax1.set_xlim(xmin1, xmax1)
    ax2.set_xlim(xmin2, xmax2)
    
    plt.savefig('voice_weekday_all.png', dpi=300)

voice() 
