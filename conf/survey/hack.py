import __main__
assert type(root)==__main__.DdtConfig, 'config is of type %s.%s instead of __main__.DdtConfig' % (type(root).__module__, type(root).__name__)
root.MaxSeeing=2.0
root.MaxProximityBonus=0.5
root.RestartLostSequences=False
root.filters={}
root.filters['i']=__main__.FilterConfig()
root.filters['i'].minBright=19.0
root.filters['i'].maxBright=30.0
root.filters['i'].name='i'
root.filters['y']=__main__.FilterConfig()
root.filters['y'].minBright=17.5
root.filters['y'].maxBright=30.0
root.filters['y'].name='y'
root.filters['r']=__main__.FilterConfig()
root.filters['r'].minBright=19.0
root.filters['r'].maxBright=30.0
root.filters['r'].name='r'
root.filters['z']=__main__.FilterConfig()
root.filters['z'].minBright=17.5
root.filters['z'].maxBright=30.0
root.filters['z'].name='z'
root.filters['g']=__main__.FilterConfig()
root.filters['g'].minBright=19.0
root.filters['g'].maxBright=30.0
root.filters['g'].name='g'
root.sequences={}
root.sequences[1]=__main__.SequenceConfig()
root.sequences[1].numSequenceEvents=1
root.sequences[1].sequenceWindowStart=-0.5
root.sequences[1].sequenceFilter=['g']
root.sequences[1].numSequenceExposures={'g': 100}
root.sequences[1].sequenceInterval=60
root.sequences[1].sequenceWindowMax=0.25
root.sequences[1].numMaxMissed=0
root.sequences[1].sequenceWindowEnd=0.5
root.sequences[1].name='continuousG'
root.sequences[2]=__main__.SequenceConfig()
root.sequences[2].numSequenceEvents=1
root.sequences[2].sequenceWindowStart=-0.5
root.sequences[2].sequenceFilter=['r']
root.sequences[2].numSequenceExposures={'r': 100}
root.sequences[2].sequenceInterval=60
root.sequences[2].sequenceWindowMax=0.25
root.sequences[2].numMaxMissed=0
root.sequences[2].sequenceWindowEnd=0.5
root.sequences[2].name='continuousR'
root.newFieldsLimitWest_beforeLSTatSunrise=0.0
root.AcceptSerendipity=False
root.userRegions={}
root.userRegions[0]=__main__.UserRegionConfig()
root.userRegions[0].diameter=0.2
root.userRegions[0].dec=-70.76
root.userRegions[0].ra=81.78
root.userRegions[1]=__main__.UserRegionConfig()
root.userRegions[1].diameter=0.2
root.userRegions[1].dec=-68.16
root.userRegions[1].ra=84.97
root.userRegions[2]=__main__.UserRegionConfig()
root.userRegions[2].diameter=0.2
root.userRegions[2].dec=-73.29
root.userRegions[2].ra=77.61
root.userRegions[3]=__main__.UserRegionConfig()
root.userRegions[3].diameter=0.2
root.userRegions[3].dec=-65.93
root.userRegions[3].ra=79.83
root.userRegions[4]=__main__.UserRegionConfig()
root.userRegions[4].diameter=0.2
root.userRegions[4].dec=-72.9
root.userRegions[4].ra=16.57
root.userRegions[5]=__main__.UserRegionConfig()
root.userRegions[5].diameter=0.2
root.userRegions[5].dec=-50.86
root.userRegions[5].ra=260.86
root.RelativeProposalPriority=5.0
root.masterSequences={}
root.masterSequences[1]=__main__.MasterSequenceConfig()
root.masterSequences[1].numSequenceEvents=3
root.masterSequences[1].sequenceWindowStart=-0.5
root.masterSequences[1].subSequence.numSequenceEvents=45
root.masterSequences[1].subSequence.sequenceWindowStart=-1.0
root.masterSequences[1].subSequence.sequenceFilter=['g', 'r']
root.masterSequences[1].subSequence.numSequenceExposures={'r': 1, 'g': 1}
root.masterSequences[1].subSequence.sequenceInterval=960
root.masterSequences[1].subSequence.sequenceWindowMax=1.0
root.masterSequences[1].subSequence.numMaxMissed=5
root.masterSequences[1].subSequence.sequenceWindowEnd=2.0
root.masterSequences[1].subSequence.name='G2R2sub'
root.masterSequences[1].sequenceWindowEnd=0.5
root.masterSequences[1].sequenceInterval=86400
root.masterSequences[1].sequenceWindowMax=0.25
root.masterSequences[1].numMaxMissed=0
root.masterSequences[1].name='G2R2master'
root.masterSequences[2]=__main__.MasterSequenceConfig()
root.masterSequences[2].numSequenceEvents=3
root.masterSequences[2].sequenceWindowStart=-0.5
root.masterSequences[2].subSequence.numSequenceEvents=45
root.masterSequences[2].subSequence.sequenceWindowStart=-1.0
root.masterSequences[2].subSequence.sequenceFilter=['g', 'r']
root.masterSequences[2].subSequence.numSequenceExposures={'r': 1, 'g': 1}
root.masterSequences[2].subSequence.sequenceInterval=960
root.masterSequences[2].subSequence.sequenceWindowMax=1.0
root.masterSequences[2].subSequence.numMaxMissed=5
root.masterSequences[2].subSequence.sequenceWindowEnd=2.0
root.masterSequences[2].subSequence.name='G2R2anothersub'
root.masterSequences[2].sequenceWindowEnd=0.5
root.masterSequences[2].sequenceInterval=86400
root.masterSequences[2].sequenceWindowMax=0.25
root.masterSequences[2].numMaxMissed=0
root.masterSequences[2].name='G2R2anothermaster'
root.minTransparency=0.7
root.AcceptConsecutiveObs=True
root.TwilightBoundary=-12.0
root.newFieldsLimitEast_afterLSTatSunset=0.0
root.EB=10.0
root.RankIdleSeq=0.1
root.ExposureTime=34.0
root.taperB=180.0
root.RankLossRiskMax=10.0
root.deltaLST=60.0
root.taperL=2.0
root.RestartCompleteSequences=False
root.maxReach=90.0
root.MaxNumberActiveSequences=100
root.MaxAirmass=2.0
root.HiatusNextNight=0
root.peakL=20.0
root.RankTimeMax=1.0
