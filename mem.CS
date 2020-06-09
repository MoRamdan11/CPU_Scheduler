    public class Memory
    {
        public int memoryLength;
        public List<Hole> holes;
        public Memory(int memoryLength)
        {
            this.memoryLength = memoryLength;
            holes = new List<Hole>();
            holes.Add(new Hole(0, memoryLength));
        }
    }

        public void deAllocate(Process p)
        {
            for (int SegmentIndex = 0; SegmentIndex < p.numberOfSegments; SegmentIndex++)
            {
                holes.Insert(0, new Hole(p.segments[SegmentIndex].Base, p.segments[SegmentIndex].length));
            }
            holes.Sort(new Comparison<Hole>((x, y) =>
            {
                return x.Base.CompareTo(y.Base);
            }));
            for (int holeIndex = 0; holeIndex < holes.Count - 1; holeIndex++)
            {
                if (holes[holeIndex].Base + holes[holeIndex].Limit == holes[holeIndex + 1].Base)
                {

                    holes[holeIndex].Limit += holes[holeIndex + 1].Limit;
                    holes.RemoveAt(holeIndex + 1);
                    holeIndex--;

                }


            }
